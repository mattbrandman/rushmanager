(function(){
	

	var app = angular.module('rankingCreation', []);
	
	app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
	}]);

	app.controller('RankingController', ['$scope', '$http', '$q', 'httpRushService', function( $scope, $http, $q, httpRushService){
		this.ranking = {};
		this.numberRange = this.range;

		//this is the list of rankings
		this.rankingList = [];
		var _this = this
		var x = httpRushService.getRushes();
		x.then(function(payload) {
			_this.listOfRushes = payload.data;
			_this.numberRange = _this.range();
			_this.ranking.rush = _this.listOfRushes[0];
		});
		var y = httpRushService.getRanks();
		y.success(function(data) {
			_this.rankingList = data;
		});

		this.range = function() {
			var result = [];
			var i;
			for(i = 1; i <= 10; i++) {
				result.push(i);
			}
			return result;
		};

		//TODO: right now i'm going to just pass in the select index
		//later this should be done in a better way
		this.addRanking = function() {
			var _this = this;
			
			//creates a map of indexes based on user id then finds the index
			//of the selected rush
			var index =  this.listOfRushes.map(function(el) {
  				return el.id;
			}).indexOf(this.ranking.rush);

			this.listOfRushes.splice(index, 1);
			$http.post('/api/ranked/', this.ranking).success(function(data) {
				_this.rankingList.unshift(data);
			});
			this.ranking = {};
			
		};

		this.remove = function(data) {
			var index  = this.rankingList.indexOf(data);
			this.rankingList.splice(index, 1);
			var url = '/api/ranked/' + data.id + '/'
			$http.delete(url);
		}

		this.update = function(data) {
			$http.patch('/api/ranked/' + data.id + '/', {'rank': data.rank});
		}
		
	}]);
	app.controller('RankGeneratorController', ['$http', '$q', function($http, $q){
		this.generateReport = function() {
			this.generatedList = [];
			var report = this;
			promise = $http.get('/api/generate-rank-list/');
			promise.success(function(data)
			{
				report.generatedList = data;
			});
		};
	}]);

	app.service('httpRushService', ['$http', function($http) {
		this.getRushes = function() {
			return $http.get('/api/ranked/get-unranked/').
			success(function(data, status, headers, config){
			//something funk with scopes and how data is formatted when returned
		});
		}
		this.getRanks = function() {
			return $http.get('/api/ranked/').
			success(function(data, status, headers, config){
			//something funk with scopes and how data is formatted when returned
		});
		}
	}]);
})();