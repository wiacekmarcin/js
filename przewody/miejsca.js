app.controller('miejsca-ctrl', ['$scope','$routeParams', '$http', function($scope, $routeParams, $http) {
    $scope.edit_place = -1;
    $scope.add_place = false;
    editRow = { id : 0 };

    $scope.sel_pom = { id : 0 , nazwa : "Wszystkie"};
    var pid = $routeParams.id;
    var get = function() {
        $http.get("miejsca_list.php?pid=" + pid).then(function(response) { 

            $scope.miejsca = response.data.miejsca;
            $scope.pomieszczenia = response.data.pomieszczenia;
            $scope.zakonczenia = response.data.zakonczenia;
            $scope.przewody = response.data.przewody;
            $scope.rodzaj = response.data.rodzaj;

            if (pid == 0)
                $scope.title = "Wszystkie";
            else if (pid == -1)
                $scope.title = "Zbiorcze";
            else if (pid == -2)
                $scope.title = "Połączenia";
            $scope.pid = pid;
        });
    };

    get();


    $scope.editPlace = function(row) {
        $scope.editRow = {
            id : row.id,
            kod : row.kod,
            nazwa : row.nazwa,
            opis : row.opis,
            polaczenie : row.polaczenie,
            zbiorcze : row.zbiorcze,
            pom : { id : row.id_pomieszczenie, nazwa : row.pomieszczenie}
        };
    }


    $scope.addPlace = function(id) {
        $scope.addRow = {
            id : -1,
            kod : '',
            nazwa : '',
            opis : '',
            polaczenie : '',
            zbiorcze : '',
            pom : { id : 0, nazwa : ''}
        };
    }

    $scope.cancelEdit = function() {
        $scope.editRow = {id : -1 };
    }

    $scope.cancelAdd = function() {
        $scope.addRow = {
            id : 0
        }
    }

    
    var toparams = function (obj) {
        var p = [];
        for (var key in obj) {
            p.push(key + '=' + encodeURIComponent(obj[key]));
        }
        return p.join('&');
    };
    
    $scope.saveEditPlace = function() {
        sendData({"id" :  $scope.editRow.id,
                  "kod" : $scope.editRow.kod,
                  "nazwa" : $scope.editRow.nazwa,
                  "id_pomieszczenie" : $scope.editRow.pom.id,
                  "opis" : $scope.editRow.opis,
                  "zbiorcze" : $scope.editRow.zbiorcze,
                  "polaczenie" : $scope.editRow.polaczenie
        });
    }

    $scope.saveAddPlace = function() {
        sendData({"id" :  $scope.addRow.id,
                  "kod" : $scope.addRow.kod,
                  "nazwa" : $scope.addRow.nazwa,
                  "id_pomieszczenie" : $scope.addRow.pom.id,
                  "opis" : $scope.addRow.opis,
                  "zbiorcze" : $scope.addRow.zbiorcze,
                  "polaczenie" : $scope.addRow.polaczenie
        });
    }

    var sendData = function(params) {
        $http({
            method: 'POST',
            url: "miejsce_add.php",
            data: toparams(params),
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        }).then( function success(response) {
            $scope.addRpw = {'id' : 0 };
            $scope.editRpw = {'id' : -1 };
        }, function error(response) {
            alert("Nie Udało się") ;
        });
    }
}]);

                                   

