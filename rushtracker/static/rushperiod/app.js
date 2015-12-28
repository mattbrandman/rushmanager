(function() {


    var app = angular.module('recruitmentPeriod', ['pikaday']);

    app.config(['$httpProvider', function($httpProvider) {
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }]);

    app.controller('RecruitmentList', ['promiseObj', function(promiseObj) {
        var _this = this;
        this.recPerList = promiseObj.data;


        this.open = function() {
            var modalInstance = $uibModal.open({
                animation: true,
                templateUrl: '/static/rushperiod/create_rushperiod.html',
                controller: "RecPerModCont as ctrl"
            });
            modalInstance.result.then(function(newItem) {
              _this.recPerList.push(newItem.data);
            });
        };  
    }]);

    app.controller('RecPerModCont', ['$uibModalInstance', '$http', function($uibModalInstance, $http) {
        var _this = this;
        this.cancel = function() {
            $uibModalInstance.dismiss('cancel');
        }
        this.onPikadayEndSelect = function(date) {
            _this.event.end_date = date.toISOString().split('T')[0];
        }
        this.onPikadayStartSelect = function(date) {
            _this.event.start_date = date.toISOString().split('T')[0];
        }
        this.save = function() {
            $http.post('/api/rushperiod/', {
                'name': _this.event.name,
                'start_date': _this.event.start_date,
                'end_date': _this.event.end_date
            }).then(function(data) {
                $uibModalInstance.close(data);
            });
        }
    }]);




    angular.module('pikaday', [])
        .provider('pikadayConfig', function pikadayProviderFn() {

            // Create provider with getter and setter methods, allows setting of global configs

            var config = {};

            this.$get = function() {
                return config;
            };

            this.setConfig = function setConfig(configs) {
                config = configs;
            };
        })
        .directive('pikaday', ['pikadayConfig', pikadayDirectiveFn]);

    function pikadayDirectiveFn(pikadayConfig) {

        return {

            restrict: 'A',
            scope: {
                pikaday: '=',
                onSelect: '&',
                onOpen: '&',
                onClose: '&',
                onDraw: '&',
                disableDayFn: '&'
            },
            link: function(scope, elem, attrs) {

                // Init config Object

                var config = {
                    field: elem[0],
                    onSelect: function() {
                        setTimeout(function() {
                            scope.$apply();
                        });
                    }
                };

                // Decorate config with globals

                angular.forEach(pikadayConfig, function(value, key) {
                    config[key] = value;
                });

                // Decorate/Overide config with inline attributes

                angular.forEach(attrs.$attr, function(dashAttr) {
                    var attr = attrs.$normalize(dashAttr); // normalize = ToCamelCase()
                    applyConfig(attr, attrs[attr]);
                });

                function applyConfig(attr, value) {
                    switch (attr) {

                        // Booleans, Integers & Arrays

                        case "setDefaultDate":
                        case "bound":
                        case "reposition":
                        case "disableWeekends":
                        case "showWeekNumber":
                        case "isRTL":
                        case "showMonthAfterYear":
                        case "firstDay":
                        case "yearRange":
                        case "numberOfMonths":
                        case "mainCalendar":

                            config[attr] = scope.$eval(value);
                            break;

                            // Functions

                        case "onSelect":
                        case "onOpen":
                        case "onClose":
                        case "onDraw":
                        case "disableDayFn":

                            config[attr] = function(date) {
                                setTimeout(function() {
                                    scope.$apply();
                                });
                                return scope[attr]({
                                    pikaday: this,
                                    date: date
                                });
                            };
                            break;

                            // Strings

                        case "format":
                        case "position":
                        case "theme":
                        case "yearSuffix":

                            config[attr] = value;
                            break;

                            // Dates

                        case "minDate":
                        case "maxDate":
                        case "defaultDate":

                            config[attr] = new Date(value);
                            break;

                            // Elements

                        case "trigger":
                        case "container":

                            config[attr] = document.getElementById(value);
                            break;

                            // Translations

                        case "i18n":

                            config[attr] = pikadayConfig.locales[value];

                    }
                }

                // instantiate pikaday with config, bind to scope, add destroy event callback

                var picker = new Pikaday(config);
                scope.pikaday = picker;
                scope.$on('$destroy', function() {
                    picker.destroy();
                });
            }
        };
    }

})();
