app.controller('polaczenieadd-ctrl', ['$scope', '$http', function($scope, $http) {
    $scope.id_miejsce = -1;
    $scope.przewody = []
    $scope.zyla2 = {};
    $scope.choose = true;
    $scope.polaczenia = [];
    $scope.przewod_id = -1;
    $http.get("polaczenie_add.php").then(function(response) { 
        $scope.zbiorcze = response.data.zbiorcze;
        $scope.polmiejsca = response.data.polmiejsca;
        $scope.zyly = response.data.zyly;
        $scope.miejsca = response.data.miejsca;
    });

    $scope.zmianaMiejsca = function() {
        $scope.przewody = this.id_miejsce.kable;
        $scope.polaczenia = $scope.polmiejsca[this.id_miejsce.id];
    }


    $scope.zmianaPolMiejsca = function() {
        $scope.przewod1 = this.zak_id.przewod_id;
        $scope.zyly1 = $scope.zyly[$scope.przewod1];
    }

    $scope.zmianaPrzewodu1 = function() {
        $scope.zyly1 = $scope.zyly[$scope.przewod1];
    }

    $scope.zmianaPrzewodu2 = function() {
        $scope.zyly2 = $scope.zyly[$scope.przewod2];
    }

    $scope.zmianaZyly2 = function(id) {
        if (id == undefined) {
            $scope.z2 = undefined;
        } else {
            if ($scope.zyla2[id] == undefined)
                $scope.z2 = undefined;
            else 
                $scope.z2 = $scope.zyla2[id].id;
        }
        $scope.z1 = id;
    }

    $scope.chooseMiejsce = function(bl) {
        $scope.choose = bl;
    }
    
    $scope.insertPolaczenia = function(zid, z1, z2)
    {
        var s1 = 'INSERT INTO `polaczenie_zyla`(`id`, `polaczenie_id`, `zyla_id_1`, `zyla_id_2`) VALUES ';
        s1 += '(NULL,' + zid + ', '  + z1 + ',' + z2 + ')';
        var s2 = 'INSERT INTO `polaczenie_zyla`(`id`, `polaczenie_id`, `zyla_id_1`, `zyla_id_2`) VALUES ';
        s2 += '(NULL, ' + zid + ', '  + z2 + ',' + z1 + ')';
        console.log(s1);
        console.log(s2);
    }

    $scope.addPolaczenie = function() {
        var params =  {'polaczenie_miejsce_id' : $scope.zak_id.id , 'count' : 0};
        var i = 0;
        for (var m in $scope.zyla2) {
            if ($scope.zyla2[m] == undefined)
                continue;
            params['id1_' + i] = m;
            params['id2_' + i] = $scope.zyla2[m].id;
            i+=1;
        }
        params['count'] = i;
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
            url: "polaczenie_ins.php",
            data: toparams(params),
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        }).then( function success(response) {
            console.log(response);
            $scope.zyla2 = {};
        }, function error(response) {
            alert("Nie Udało się") ;
        });
    }

}]);