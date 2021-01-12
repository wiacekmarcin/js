app.controller('zlacza-ctrl', ['$scope', '$http', function($scope, $http) {
    $scope.selectZbiorcze = -1;
    $scope.zlacza = [];
    $scope.detailsAll = false;
    $scope.editRow = -1;
    $scope.chooseName = "Wszystko";
    $scope.add = false;
    $scope.editZlId = -1;
    $scope.editZyla = {};
    $scope.selectedZlaczeId = -1;
    $scope.zylyedytowane = [];
    $scope.selectedit = [];
    $scope.iseditcorret = true;
    $scope.cntZylaEdit = 0;
    $scope.miejsceIdEdit = -1;

    $http.get("zlacza_list.php").then(function(response) { 
        $scope.zbiorcze = response.data.zbiorcze;
        $scope.przewody = response.data.przewody;
        $scope.zlacza = response.data.zlacza;
        $scope.zyly = response.data.zyly;
        $scope.miejsca = response.data.miejsca;
        $scope.allzyly = response.data.allzyly;
    });

    $scope.filterZlacze = function(item) 
    {
        if ($scope.selectZbiorcze == -1)
            return true;
        else
            return $scope.selectZbiorcze == item.miejsce_id;
    }

    $scope.choose = function(id, name, pom)
    {
        $scope.selectZbiorcze = id;
        $scope.chooseName = pom + " : " + name;
    }

    $scope.chooseAll = function()
    {
        $scope.selectZbiorcze = -1;
        $scope.chooseName = "Wszystko";
    }

    $scope.setDetails = function(id) 
    {
        $scope.selectedZlaczeId = id;
    }

    $scope.setDetailsAll = function() 
    {
        $scope.detailsAll = !$scope.detailsAll;
    }
    
    $scope.addZlacze = function(przewod_id, miejsce_id, il)
    {
        $scope.add = true;
        $scope.miejsceIdEdit = miejsce_id;
        $scope.cntZylaEdit = il;
        $scope.zylyedytowane = $scope.allzyly[przewod_id] || [];
        $scope.editEtykieta = '';
        $scope.editZyla = {};
        $scope.selectedPrzewodId = przewod_id;
        for (var i =0; i < $scope.zylyedytowane.length; i++) {
            var item = $scope.zylyedytowane[i];
            var zid = item.zid;
            var pos = i+1;
            $scope.zylyedytowane[i].pos = pos;
            var opis = item.cname + ' ' + item.opis;
            var mitem = { "zid" : zid, "pos" : pos,  'opis' : opis};


            $scope.editZyla[pos] = mitem;
            $scope.selectedit[i] = mitem;
        }

    }
    $scope.editZlacze = function(zlacze) 
    {
        $scope.zylyedytowane = $scope.zyly[zlacze.zlacze_id];
        $scope.selectedit = [];
        $scope.editZlId = zlacze.zlacze_id;
        $scope.editEtykieta = zlacze.etykieta;
        $scope.editZyla = {};
        $scope.cntZylaEdit = $scope.zyly[zlacze.zlacze_id].length;
        $scope.miejsceIdEdit = zlacze.miejsce_id;
        for (var i =0; i < $scope.zyly[zlacze.zlacze_id].length; i++) {
            var item = $scope.zyly[zlacze.zlacze_id][i];
            var zid = item.zid;
            var pos = item.pos;
            var opis = item.cname + ' ' + item.opis;
            var mitem = { "zid" : zid, "pos" : pos,  'opis' : opis};


            $scope.editZyla[pos] = mitem;
            $scope.selectedit[i] = mitem;
        }
    }

    $scope.checkZlacze = function() {
        var s  = [];
        var err = false;
        for (var i =0; i < $scope.cntZylaEdit; i++) 
        {
            if ($scope.editZyla[i+1]) {
                var it = $scope.editZyla[i+1];
                if (s.indexOf(it.zid) >= 0) {
                    err = true;
                    break;
                } else {
                    s.push(it.zid);
                }
            } else {
                err = true;
                break;
            }
        }
        $scope.iseditcorret = !err;
    }

    $scope.saveEdit = function()
    {
        var params = {"zlacze_id" : $scope.editZlId,
                    "etykieta" : $scope.editEtykieta,
                    "update" :  !$scope.add ,
                    "miejsce_id" : $scope.miejsceIdEdit,
                    "cnt" : $scope.cntZylaEdit};
        
        angular.forEach($scope.editZyla, function(value, key) {
                        this['pos_'+key] = value.zid;
                      }, params);
        console.log(params);
    }
    
    $scope.cancelEdit = function()
    {
        $scope.add = false;
        $scope.editZlId = -1;
        $scope.editZyla = {};
        $scope.editEtykieta = '';

        $scope.miejsceIdEdit = -1;
        $scope.cntZylaEdit = 0;
        $scope.zylyedytowane = [];
        $scope.selectedPrzewodId = -1;
        $scope.selectedit = [];
        
    }
}]);