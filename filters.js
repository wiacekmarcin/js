app.filter('przewod', ['$sce', function($sce) {
    return function(x) {
        var s, d, j;
        var l = parseInt(x, 10);
        s = Math.floor(l / 100);
        d = Math.floor((l - s*100) / 10);
        j = l - s*100 - d*10;

        var znak = ["","&#10102;","&#10103;","&#10104;","&#10105;","&#10106;","&#10107;","&#10108;","&#10109;","&#10110;"];
        
        return $sce.trustAsHtml(znak[s] + znak[d] + znak[j]);
    };
  }]);
  app.filter('toArray', function () {
    return function (obj, addKey) {
      if (!angular.isObject(obj)) return obj;
      if ( addKey === false ) {
        return Object.keys(obj).map(function(key) {
          return obj[key];
        });
      } else {
        return Object.keys(obj).map(function (key) {
          var value = obj[key];
          return angular.isObject(value) ?
            Object.defineProperty(value, '$key', { enumerable: false, value: key}) :
            { $key: key, $value: value };
        });
      }
    };
  });