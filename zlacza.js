app.controller('zlacza-ctrl', ['$scope', '$http', function($scope, $http) {
    $scope.selectZbiorcze = -1;
    $scope.zlacza = [];
    $scope.detailsAll = false;
    $scope.editRow = -1;
    $scope.chooseName = "Wszystko";
    $http.get("zlacza_list.php").then(function(response) { 
        $scope.zbiorcze = response.data.zbiorcze;
        $scope.przewody = response.data.przewody;
        $scope.zlacza = response.data.zlacza;
        $scope.zyly = response.data.zyly;
        $scope.miejsca = response.data.miejsca;
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
        $scope.detailsAll = true;
    }
}]);