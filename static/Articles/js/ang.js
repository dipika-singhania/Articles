var app = angular.module('myApp', []);
app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('/{/');
    $interpolateProvider.endSymbol('/{/');
});
app.controller('apiHitCtrl', function($scope,$http,$filter) {
	$scope.index = 0;
	$scope.forDisabled = false;
	$scope.backDisabled = false;
	$scope.decreaseIndex = function(len) {
		if( $scope.index - 4 <= 0)
			$scope.backDisabled = true;
		else 
			$scope.index = $scope.index - 4;
	}
	$scope.increaseIndex = function(len) {
		if( $scope.index + 4 >= len)
			$scope.forDisabled = true;
		else
			$scope.index = $scope.index + 4;
	}
});