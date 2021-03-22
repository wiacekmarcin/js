app.controller('zakonczeniepinyadd-ctrl', ['$scope', '$routeParams', '$location', '$http', 
function($scope, $routeParams, $location, $http) {
    $scope.zid = $routeParams.id;

    $http.get("zakonczenie_piny_add.php?zid="+$scope.zid).then(function(response) { 
        $scope.zakonczenie = response.data.zakonczenie[0];
        $scope.zyly = response.data.zyly;
        $scope.zakonczeniazylyOrg = response.data.zakonczeniaz_zyly;

        var zyly = {};
        for (var i = 0; i < $scope.zyly.length; i++) {
            zyly[$scope.zyly[i].id] = $scope.zyly[i];
        }

        $scope.zakonczeniazyly = [];
        for (var i = 0; i < $scope.zakonczenie.ilosc; i++) {
            $scope.zakonczeniazyly.push({pos: i+1, 
                opis: i+1, kolor:'', html:'', 
                zyla_id:-1, id:-1, zyla : {}
            });
        }

        for (var i = 0; i < $scope.zyly.zakonczeniazylyOrg; i++) {
            var item = $scope.zyly.zakonczeniazylyOrg[i];
            $scope.zakonczeniazyly[item.pos-1].opis = item.opis;
            $scope.zakonczeniazyly[item.pos-1].zyla_id = item.zyla_id;
            $scope.zakonczeniazyly[item.pos-1].id = item.id;
            $scope.zakonczeniazyly[item.pos-1].zyla = zyly[item.zyla_id];

        }

    });

}]);