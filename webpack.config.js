var path = require("path");
var webpack = require("webpack");
var BundleTracker = require('webpack-bundle-tracker');
var CleanWebpackPlugin = require('clean-webpack-plugin');
// const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;

module.exports = {
  context: __dirname,

  entry: {
    main: './react/index.js',
  },

  output: {
    path: path.resolve('./core/static/core/js/bundle'),
    filename: "[name]-[chunkhash].js",
  },

  optimization: {
    splitChunks: {
      chunks: 'all',
    },
  },

  plugins: [
    new BundleTracker({filename: './webpack-stats.json'}),
    //new BundleAnalyzerPlugin(),
  ],

  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
        }
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader']
      },
    ]
  },
  resolve: {
    extensions: ['*', '.js', '.jsx']
  },
};
