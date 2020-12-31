app.controller('miejsca-ctrl', ['$scope','$routeParams', '$http', function($scope, $routeParams, $http) {
    $scope.edit_place = -1;
    $scope.add_place = false;
    $scope.sel_pom_id = 0;
    var get = function() {
        $http.get("miejsca_list.php").then(function(response) { 

            $scope.miejsca = response.data.miejsca;
            $scope.pomieszczenia = response.data.pomieszczenia;
            $scope.zakonczenia = response.data.zakonczenia;
            $scope.przewody = response.data.przewody;
            $scope.rodzaj = response.data.rodzaj;

            $scope.title = "Wszystkie";
        });
    };

    get();

    $scope.wybierzPomieszczenie = function(pid) {
        $scope.sel_pom_id = 1;
    }


    $scope.editPlace = function(row) {
        $scope.edit_place = row.id;
        $scope.ename = row.nazwa;
        $scope.epomieszczenie = row.id_pomieszczenie;
        $scope.edescription = row.opis;
        $scope.ekod = row.kod;
        $scope.epolaczenie = row.polaczenie;
        $scope.ezbiorcze = row.zbiorcze;
    }

    $scope.addPlace = function(id) {
        $scope.add_place = true;
    }

    $scope.canceleditPlace = function() {
        $scope.edit_place = -1;
    }

    $scope.canceladdPlace = function() {
        $scope.add_place = false;
        $scope.akod = "";
        $scope.aname = "";
        $scope.apomieszczenie = -1;
        $scope.adescription = "";
        $scope.azbiorcze = "";
        $scope.apolaczenie = "";
    }

    
    var toparams = function (obj) {
        var p = [];
        for (var key in obj) {
            p.push(key + '=' + encodeURIComponent(obj[key]));
        }
        return p.join('&');
    };
    
    $scope.savePlace = function() {
        sendData({"id" :  $scope.edit_place,
                  "kod" : $scope.ekod,
                  "nazwa" : $scope.ename,
                  "id_pomieszczenie" : $scope.epomieszczenie,
                  "opis" : $scope.edescription,
                  "zbiorcze" : $scope.ezbiorcze,
                  "polaczenie" : $scope.epolaczenie
        });
    }

    $scope.addnewPlace = function() {
        sendData({"id" :  -1,
                  "kod" : $scope.akod,
                  "nazwa" : $scope.aname,
                  "id_pomieszczenie" : $scope.apomieszczenie,
                  "opis" : $scope.adescription,
                  "zbiorcze" : $scope.azbiorcze,
                  "polaczenie" : $scope.apolaczenie
        });
    }

    var sendData = function(params) {
        $http({
            method: 'POST',
            url: "miejsce_add.php",
            data: toparams(params),
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        }).then( function success(response) {
            $scope.akod = "";
            $scope.aname = "";
            $scope.apomieszczenie = -1;
            $scope.adescription = "";
            $scope.azbiorcze = "";
            $scope.apolaczenie = "";
            $scope.add_place = false;
            $scope.edit_place = -1;
        }, function error(response) {
            alert("Nie Udało się") ;
        });
    }
}]);

                                   

