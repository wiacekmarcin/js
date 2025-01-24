app.controller('zakonczeniepinyadd-ctrl', ['$scope', '$routeParams', '$location', '$http', 
function($scope, $routeParams, $location, $http) {
    $scope.zid = $routeParams.id;

    $http.get("zakonczenie_piny_add.php?zid="+$scope.zid).then(function(response) { 
        $scope.zakonczenie = response.data.zakonczenie[0];
        $scope.zyly = response.data.zyly;
        $scope.zakonczeniazylyOrg = response.data.zakonczeniaz_zyly;

        $scope.zyly.push({id:-1, kolor_id:0, opis:'Brak żyly', kolor:"nieoznaczony", html:'gray'});

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

        for (var i = 0; i < $scope.zakonczeniazylyOrg.length; i++) {
            var item = $scope.zakonczeniazylyOrg[i];
            $scope.zakonczeniazyly[item.pos-1].opis = item.opis;
            $scope.zakonczeniazyly[item.pos-1].zyla_id = item.zyla_id;
            $scope.zakonczeniazyly[item.pos-1].id = item.id;
            $scope.zakonczeniazyly[item.pos-1].zyla = zyly[item.zyla_id];
            $scope.zakonczeniazyly[item.pos-1].pos = item.pos;
        }

    });

    $scope.savePins = function() {
        params = { 'length': $scope.zakonczeniazyly.length, 'zkid': $scope.zid};        
        for (var i = 0; i < $scope.zakonczeniazyly.length; i++) {
            var item = $scope.zakonczeniazyly[i];
            params["opis_" + i] = item.opis;
            params["zyla_id_" + i] = item.zyla.id;
            params["id_" + i] = item.id;
            params["pos_" + i] = item.pos;

        }
        sendData(params);
    }

    $scope.reset = function() {
        $location.path("index.html");
    }

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
            url: "zakonczenie_piny_add_ins.php",
            data: toparams(params),
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        }).then( function success(response) {
            $scope.reset();
        }, function error(response) {
            alert("Nie Udało się") ;
        });
    };

}]);