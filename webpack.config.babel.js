import ExtractTextPlugin from 'extract-text-webpack-plugin';
import webpack from 'webpack';
import autoprefixer from "autoprefixer";

const dev = JSON.parse(process.env.BUILD_DEV || 'false');


module.exports = {
  entry: {
    vendor: [
      'bootstrap',
    ],
    all: [
      './core/static/scss/all.scss',
      './core/static/js/app.js',
    ],
  },

  output: {
    path: `${__dirname}/static/`,
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
        test: /\.(woff2?|ttf|eot|svg|jpg|png|gif|swf)(\?.*)?$/,
        loader: 'file-loader',
      },
      {
        test: /\.js$/,
        exclude: /node_modules/,
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
  ],
};