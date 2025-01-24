app.controller('zakonczenieadd-ctrl', ['$scope', '$routeParams', '$location', '$http', 
function($scope, $routeParams, $location, $http) {
    $scope.pmid = $routeParams.id;
    $scope.zid = -1;
    $http.get("zakonczenie_add.php?pmid="+$scope.pmid).then(function(response) { 
        $scope.rodzaj_zakonczenia = response.data.rodzaj_zakonczenia;
        $scope.przewod = response.data.zakonczenie[0].przewod;
        $scope.popis = response.data.zakonczenie[0].popis;
        $scope.miejse = response.data.zakonczenie[0].miejsce;
        $scope.ilosc = response.data.zakonczenie[0].ilosc;
    });

    $scope.master = {};

    $scope.update = function(zakonczenie) {
        var params = { "zid" : $scope.zid,
                    "pmid" : $scope.pmid,
                    "etykieta" : zakonczenie.nazwa,
                    "rodzaj_zakonczenia" : zakonczenie.rodzaj.id,
                    "ilosc_pin" : zakonczenie.ilosc_pinow
                };
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
            var zik = response.data.zid;
            console.log("zik");
            $location.path("zakonczenie_piny_add/" + zik);
        }, function error(response) {
            alert("Nie Udało się") ;
        });
    }
}]);