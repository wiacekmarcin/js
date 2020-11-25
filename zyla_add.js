app.controller('zylaadd-ctrl', ['$scope', '$http', function($scope, $http) {
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
        }
    }

    $scope.chooseZyla = function(index) {
        $scope.selectedHtml[index] = $scope.selectedKolor[index].html;
    }


    $scope.dodajDoBazy = function() {
        var przewod_id = $scope.przewod_id.id;
        var zyly = [];
        for (var i = 0; i < $scope.przewod_id.ilosc_zyl; i++) {
            zyly.push({'id' : $scope.selectedZid[i], 'cid': $scope.selectedKolor[i].id, 'opis': $scope.selectedOpis[i]});
        }
        console.log(zyly);
    }
}]);