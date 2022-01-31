const { dest, series, src, watch } = require('gulp');
const autoprefixer = require('autoprefixer');
const cssnano = require('cssnano');
const less = require('gulp-less');
const postcss = require('gulp-postcss');

const base_src = './kulupulang/static/src/'
const base_dist = './kulupulang/static/dist/'

function lessTask() {
    return src(`${base_src}less/base.less`, {base: `${base_src}less/`})
        .pipe(less())
        .pipe(postcss([autoprefixer(), cssnano()]))
        .pipe(dest(`${base_dist}css`));
}

function watchTask() {
    watch(`${base_src}less/**/*.less`, { ignoreInitial: true }, lessTask);
}

exports.less = lessTask;
exports.watch = watchTask;
exports.all = series(lessTask)
exports.default = watchTask;
