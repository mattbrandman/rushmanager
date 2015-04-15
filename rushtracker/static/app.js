(function(){
	var app = angular.module('rankingCreation', []);
	app.controller('RankingController', ['$scope', '$http', '$q', 'httpRushService', function( $scope, $http, $q, httpRushService){
		this.ranking = {};
		this.rankList = this.range;
		//this is the list of rankings
		this.rankingList = [];
		var _this = this
		var x = httpRushService.getRushes();
		x.then(function(payload) {
			_this.listOfRushes = payload.data;
			_this.rankList = _this.range();
		});

		this.range = function() {
			var result = [];
			var i;
			for(i = 1; i <= this.listOfRushes.length; i++) {
				result.push(i);
			}
			return result;
		};

		this.addRanking = function() {
			this.rankingList.push(this.ranking);
			this.listOfRushes.splice(this.listOfRushes.indexOf(this.ranking.rush), 1);
			this.rankList.splice(this.rankList.indexOf(this.ranking.rank), 1);
			this.ranking = {};
			
		};

		
	}]);


	app.service('httpRushService', ['$http', function($http) {
		this.getRushes = function() {
			return $http.get('/api/rush/').
			success(function(data, status, headers, config){
			//something funk with scopes and how data is formatted when returned
		});
		}
	}]);
})();