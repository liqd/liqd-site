import os
import logging
from compressor.filters import CompilerFilter
from django.conf import settings

logger = logging.getLogger(__name__)


class SassMapFilter(CompilerFilter):

    '''
    Filter for running a sass precompiler with the --sourcemap option.
    The default CompilerFilter would run the command with a temporary
    outfile directory, which is also where the source maps would be written.

    This filter changes the outfile to be the location of the final
    compiled css file using paths from django settings.

    See:
        https://developers.google.com/chrome-developer-tools/docs/css-preprocessors
        https://medium.com/what-i-learned-building/b4daab987fb0

    Important:
    ==========
    CSS compression must be turned off for this to function correctly.
    Compression combines multiple css files into one, which is a separate
    process which SASS is unaware of.

        COMPRESS_ENABLED = False

    If COMPRESS_ENABLED is True, then the maps will still be output correctly,
    but browsers can't handle multiple `sourceMappingURL`s in the resulting file.

    There is a concept of `sections` which is an alternative representation to support
    multiple maps, but again, SASS doesn't know this is happening so a different
    pre-compiler/minifier processor would be required that can track the state
    of multiple file compilations and concatenation.

    Usage:
    ======

    Include the module path to this filter in your COMPRESS_PRECOMPILERS,
    e.g.:

        COMPRESS_PRECOMPILERS = (
            ('text/x-scss', 'contrib.sass.SassMapFilter'),
            ...
        )
    '''

    # cd to the static root so that sass can find included libraries
    # --scss for the type of sass files we're processing
    # --sourcemap generates the .map file in the same directory as outfile
    command = "cd {static_root}; sass --style compressed --sourcemap {infile} {outfile}"

    options = (
        ("static_root", settings.STATIC_ROOT),
        ("output_dir", settings.COMPRESS_OUTPUT_DIR),
    )

    def __init__(self, content, command=None, *args, **kwargs):
        # Command comming into handlebars filter is actually the
        # Django-compressor sends the attribudes dict as the command in this
        # case, which is fine, as we need it, but it's kind of wonky. So, ensure
        # things are setup appropriately.
        attribs, command = command, None
        for item in attribs.iteritems():
            self.options += (item,)
        super(SassMapFilter, self).__init__(
            content, command=command, *args, **kwargs)

    def input(self, **kwargs):
        # Sass will create the sourcemap wherever the file is output,
        # so we want that to be where the final CSS will exist.
        # The default CompilerFilte will use a temporary outfile name
        # unless one is supplied, which we do below.
        options = dict(self.options)
        filename = os.path.basename(self.filename)
        outfilename = os.path.splitext(
            filename)[0] + '.' + options['filter_type']
        outdir = os.path.join(
            options['static_root'], options['output_dir'], options['filter_type'])
        outfile = os.path.join(outdir, outfilename)
        self.options += (('outfile', outfile),)
        return super(SassMapFilter, self).input(**kwargs)
