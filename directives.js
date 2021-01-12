app.directive('simpleHtml', function() {
    return function(scope, element, attr) {
      scope.$watch(attr.simpleHtml, function (value) {
        element.html(scope.$eval(attr.simpleHtml));
      })
    };
  })
  .directive('stringToNumber', function() {
    return {
      require: 'ngModel',
      link: function(scope, element, attrs, ngModel) {
        ngModel.$parsers.push(function(value) {
          return '' + value;
        });
        ngModel.$formatters.push(function(value) {
          return parseFloat(value);
        });
      }
    };
  });