const ExtractTextPlugin = require("extract-text-webpack-plugin")
const webpack = require("webpack")
const autoprefixer = require("autoprefixer")

const dev = JSON.parse(process.env.BUILD_DEV || 'false');


module.exports = {
  entry: {
    vendor: [
      'bootstrap/js/src/util',
      'bootstrap/js/src/collapse',
      'jquery/dist/jquery.min.js',
    ],
    all: [
      './apps/core/static/scss/all.scss',
      './apps/core/static/js/app.js',
    ],
  },

  output: {
    path: `${__dirname}/website_wagtail/static/`,
    publicPath: '/static/',
    filename: '[name].js',
  },

  module: {
    loaders: [
      {
        test: /\.css$/,
        loader: ExtractTextPlugin.extract({ fallback: 'style-loader', use: [
          'css-loader',
            {
              loader: 'postcss-loader',
              options: {
                plugins: [
                  autoprefixer(),
                ]
              }
            }
        ]}),
      },
      {
        test: /\.scss/,
        loader: ExtractTextPlugin.extract({ fallback: 'style-loader', use: 'css-loader!sass-loader' }),
      },
      {
        test: /\.(vs|fs)$/,
        include: /liquid-logo/,
        loader: 'raw-loader'
      },
      {
        test: /\.(vs|fs)$/,
        include: /liquid-logo/,
        loader: 'glslify-loader'
      },
      {
        test: /\.(woff2?|ttf|eot|svg|jpg|png|gif|swf|otf)(\?.*)?$/,
        loader: 'file-loader',
      },
      {
        test: /\.js$/,
        exclude: /node_modules\/(?!(bootstrap|liquid-logo))/,
        loader: 'babel-loader',
        query: {
          cacheDirectory: true,
          presets: ['es2015'],
          plugins: [
            'syntax-object-rest-spread',
            'transform-object-rest-spread',
          ],
        },
      },
    ],
  },

  plugins: [
    new webpack.DefinePlugin({
      dev: JSON.stringify(dev),
      'process.env.NODE_ENV': dev ? '"development"' : '"production"',
    }),
    new webpack.ContextReplacementPlugin(/moment[/\\]locale$/, /cs/),
    new ExtractTextPlugin('[name].css'),
    new webpack.ProvidePlugin({
      $: "jquery",
      jQuery: "jquery"
    })
  ],
};
