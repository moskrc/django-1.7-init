var gulp = require('gulp'),
    nib = require('nib'),
    stylus = require('gulp-stylus'),
    csso = require('gulp-csso'),
    concat = require('gulp-concat');


gulp.task('stylus', function () {
    gulp.src('./main.styl')
        .pipe(stylus({use: [nib()]}))
        .on('error', console.log)
        .pipe(gulp.dest('../css/'))
});

gulp.task('watch', function() {
    gulp.run('stylus');

        gulp.watch('./*.styl', function() {
            gulp.run('stylus');
        });
//    gulp.run('http-server');
});
