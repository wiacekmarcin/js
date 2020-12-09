app.controller('zakonczenieadd-ctrl', ['$scope', '$routeParams', '$location', '$http', 
function($scope, $routeParams, $location, $http) {
    $scope.pmid = $routeParams.id;
    $scope.zid = -1;
    $http.get("zakonczenie_add.php").then(function(response) { 
        $scope.rodzaj_zakonczenia = response.data.rodzaj_zakonczenia;
    });

    $scope.master = {};

    $scope.update = function(zakonczenie) {
        var params = { "zid" : $scope.zid,
                    "pmid" : $scope.pmid,
                    "etykieta" : zakonczenie.nazwa,
                    "rodzaj_zakonczenia" : zakonczenie.rodzaj.id };
        sendData(params);
    };

    $scope.reset = function() {
        $scope.zakonczenie = angular.copy($scope.master);
     };

    $scope.reset();

    var toparams = function (obj) {
        var p = [];
        for (var key in obj) {
            p.push(key + '=' + encodeURIComponent(obj[key]));
        }
        return p.join('&');
    };

    var sendData = function(params) {
        $http({
            method: 'POST',
            url: "zakonczenie_ins.php",
            data: toparams(params),
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        }).then( function success(response) {
            $scope.reset();
            var zik = response.data.zik;
            console.log("zik");
        }, function error(response) {
            alert("Nie Udało się") ;
        });
    }
}]);