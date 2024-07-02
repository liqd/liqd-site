const webpack = require('webpack')
const path = require('path')
const autoprefixer = require('autoprefixer')
const MiniCssExtractPlugin = require('mini-css-extract-plugin')

module.exports = {
  entry: {
    vendor: [
      'bootstrap/js/dist/util',
      'bootstrap/js/dist/collapse',
      'jquery/dist/jquery.min.js'
    ],
    all: [
      './apps/core/static/scss/all.scss',
      './apps/core/static/js/app.js'
    ],
    matomo: [
      './apps/core/static/js/matomo.js'
    ]
  },

  output: {
    libraryTarget: 'this',
    library: '[name]',
    path: path.resolve('./website_wagtail/static/'),
    publicPath: '/static/',
    filename: '[name].js'
  },

  module: {
    rules: [
      {
        test: /\.s?css$/,
        use: [
          {
            loader: MiniCssExtractPlugin.loader
          },
          {
            loader: 'css-loader'
          },
          {
            loader: 'postcss-loader',
            options: {
              postcssOptions: {
                plugins: [
                  autoprefixer
                ]
              }
            }
          },
          {
            loader: 'sass-loader'
          }
        ]
      },
      {
        test: /\.(glsl|vs|fs|vert|frag)$/,
        include: /liquid-logo/,
        use: ['raw-loader', 'glslify-loader']
      },
      {
        test: /\.(woff2?|ttf|eot|svg|jpg|png|gif|swf|otf)(\?.*)?$/,
        type: 'asset/resource'
      }
    ]
  },
  resolve: {
    extensions: ['*', '.js', '.jsx', '.scss', '.css'],
    // when using `npm link`, dependencies are resolved against the linked
    // folder by default. This may result in dependencies being included twice.
    // Setting `resolve.root` forces webpack to resolve all dependencies
    // against the local directory.
    modules: [path.resolve('./node_modules')]
  },
  plugins: [
    new webpack.ContextReplacementPlugin(/moment[/\\]locale$/, /cs/),
    new webpack.ProvidePlugin({
      $: 'jquery',
      jQuery: 'jquery'
    }),
    new MiniCssExtractPlugin({
      filename: '[name].css',
      chunkFilename: '[id].css'
    })
  ]
}
