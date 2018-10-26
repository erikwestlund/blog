let mix = require('laravel-mix');
let tailwindcss = require('tailwindcss');
let glob = require("glob-all");
let PurgecssPlugin = require("purgecss-webpack-plugin");

// Custom PurgeCSS extractor for Tailwind that allows special characters in
// class names.
//
// https://github.com/FullHuman/purgecss#extractor
class TailwindExtractor {
    static extract(content) {
        return content.match(/[A-Za-z0-9-_:\/]+/g) || [];
    }
}

mix.setPublicPath('./app')
    .sass('resources/sass/app.scss', 'app/app/static')
    .options({
        processCssUrls: false,
        postCss: [tailwindcss('./tailwind.js')],
    })
    .js('resources/js/app.js', 'app/app/static')
    .extract([
        'vue',
        'axios',
        'lodash'
    ])
    .sourceMaps()
    .version();

if (mix.inProduction()) {
  mix.webpackConfig({
    plugins: [
      new PurgecssPlugin({

        // Specify the locations of any files you want to scan for class names.
        paths: glob.sync([
          path.join(__dirname, "app/app/**/*.html"),
          path.join(__dirname, "resources/js/**/*.vue")
        ]),
        extractors: [
          {
            extractor: TailwindExtractor,

            // Specify the file extensions to include when scanning for
            // class names.
            extensions: ["html", "js", "py", "vue"]
          }
        ]
      })
    ]
  });
}