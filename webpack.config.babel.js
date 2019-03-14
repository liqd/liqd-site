const MiniCssExtractPlugin = require('mini-css-extract-plugin')
const webpack = require("webpack")
const path = require('path')
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
    rules: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules\/(?!(bootstrap)\/).*/,
        loader: 'babel-loader',
        options: {
          presets: ['@babel/preset-env', '@babel/preset-react'].map(require.resolve),
          plugins: ['@babel/plugin-transform-runtime', '@babel/plugin-transform-modules-commonjs']
        }
      },
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
              ident: 'postcss',
              plugins: (loader) => [
                autoprefixer()
              ]
            }
          },
          {
            loader: 'sass-loader'
          }
        ]
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
      }
    ],
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
    new webpack.DefinePlugin({
      dev: JSON.stringify(dev),
      'process.env.NODE_ENV': dev ? '"development"' : '"production"',
    }),
    new webpack.ContextReplacementPlugin(/moment[/\\]locale$/, /cs/),
    new MiniCssExtractPlugin({
      filename: '[name].css',
      chunkFilename: '[id].css'
    }),
    new webpack.ProvidePlugin({
      $: "jquery",
      jQuery: "jquery"
    })
  ],
};
