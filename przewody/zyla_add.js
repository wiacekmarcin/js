app.controller('zylaadd-ctrl', ['$scope', '$routeParams', '$location', '$http', 
function($scope, $routeParams, $location, $http) {
    var pid = $routeParams.id;
    
    $scope.przewod_id = -1;

    $scope.selectedId = {};
    $scope.selectedZyla = false;


    $scope.selectedKolor = {};
    $scope.selectedOpis = {};
    $scope.selectedHtml = {};
    $scope.selectedZid = {};
    $http.get("zyla_add.php").then(function(response) { 
        $scope.przewody = response.data.przewody;
        $scope.colors = response.data.colors;
        if (pid != -1) {
            for (var i = 0; i < $scope.przewody.length; i++) {
                for (var j = 0; j < $scope.przewody[i].length; j++) {
                    if ($scope.przewody[i][j].id == pid) {
                        $scope.przewod_id = $scope.przewody[i][j];
                        $scope.dodajZyly(true);
                        j = $scope.przewody[i].length;
                        i = $scope.przewody.length;
                    }
                }
            }
        }
    });

    $scope.choosePrzewod = function(index)
    {
        $scope.przewod_id = $scope.selectedId[index];
        for (var sel in $scope.selectedId) {
            if (sel == index)
                continue;
            $scope.selectedId[sel] = undefined;
        }
    }

    $scope.getNumber = function(num) {
        var tmp = [];
        for (var i=0; i<num; i++) {
            tmp.push(i);
        }
        return tmp;   
    }

    $scope.dodajZyly = function(b) {
        $scope.selectedZyla = b;
        if (b) {
            $http.get("zyla_get.php?pid=" + $scope.przewod_id.id).then(function(response) { 
                $scope.selectedKolor = {};
                $scope.selectedHtml = {};
                $scope.selectedOpis = {};
                $scope.selectedZid = {};
                for (var n = 0; n < response.data.zyly.length; n++)
                {
                    item = response.data.zyly[n];
                    $scope.selectedKolor[n] = {'id' : item['cid'], 'cname' : item['cname'], 'html': item['html']};
                    $scope.selectedHtml[n] = item['html'];
                    $scope.selectedOpis[n] = item['opis'];
                    $scope.selectedZid[n] = item['id'];
                }
            });
        } else {
            $scope.przewod_id = -1;
            $scope.selectedId = {};
            $location.path("zyla_add/-1");
        }
    }

    $scope.chooseZyla = function(index) {
        $scope.selectedHtml[index] = $scope.selectedKolor[index].html;
    }


    $scope.dodajDoBazy = function() {
        var params =  {'przewod' : $scope.przewod_id.id , 'count' : $scope.przewod_id.ilosc_zyl};
        for (var i = 0; i < $scope.przewod_id.ilosc_zyl; i++) {
            params['id_' + i] = $scope.selectedZid[i] ? $scope.selectedZid[i] : '-1'; 
            params['kolor_' + i] = $scope.selectedKolor[i].id;
            params['opis_' + i] = $scope.selectedOpis[i] ? $scope.selectedOpis[i] : '';
        }
        sendData(params);
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
            url: "zyla_ins.php",
            data: toparams(params),
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        }).then( function success(response) {
            console.log(response);
            $scope.dodajZyly(false);
        }, function error(response) {
            alert("Nie Udało się") ;
        });
    }
}]);


