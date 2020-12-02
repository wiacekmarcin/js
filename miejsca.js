app.controller('miejsca-ctrl', ['$scope','$routeParams', '$http', function($scope, $routeParams, $http) {
    var mid = $routeParams.id;
    $scope.edit_place = -1;
    $scope.add_place = false;
    $http.get("miejsca_list.php?pid="+ mid).then(function(response) { 
        $scope.places = response.data.miejsca;
        $scope.pomieszczenia = response.data.pomieszczenia;

        if (mid == -1) {
            $scope.title = "Wszystkie";
            $scope.show_place = true;
        } else if (mid == 0) {
            $scope.title = "Zbiorcze";
            $scope.show_place = true;
        } else {
            $scope.show_place = false;
            for (var i=0; i < $scope.pomieszczenia.length; i++) {
                if ($scope.pomieszczenia[i].id == mid) {
                    $scope.title = $scope.pomieszczenia[i].nazwa;
                    break;
                }
            }
        }
    });

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

/*
                                    'name' => $row['name'], 
                                    'pomieszczenie' => $row['pomieszczenie'], 
                                    'id_pomieszczenie' => $row['id_pomieszczenie'], 
                                    'description' => $row['description'], 
                                    'zbiorcze' => $row['zbiorcze'], 
                                    'kod' => $row['kod'], 
                                    'polaczenie' => $row['polaczenie'],
                                    'kable' => array()
                                    
*/                                    

