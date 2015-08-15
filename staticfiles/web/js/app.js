(function () {
    'use strict';
    angular
        .module('app', ['ngRoute', 'ngMaterial', 'ngAnimate'])
        .config(function ($mdThemingProvider) {
            $mdThemingProvider
                .theme('default')
                .primaryPalette('green')
                .accentPalette('orange');
        })
        .config(['$mdIconProvider', function ($mdIconProvider) {
            $mdIconProvider
                .iconSet('action', '/static/web/icons/action.svg', 24)
                .iconSet('navigation', '/static/web/icons/navigation.svg', 24);
                /*
                .iconSet('action', 'svg/action-icons.svg')
                .iconSet('device', 'svg/device-icons.svg')
                .iconSet('content', 'svg/content-icons.svg')
                .iconSet('alert', 'svg/alert-icons.svg')
               .iconSet('image', 'svg/image-icons.svg');*/
        }])
        .config(['$routeProvider', '$locationProvider',
            function($routeProvider, $locationProvider) {
                $routeProvider
                    .when('/recipes', {
                        templateUrl: '/visit/recipe',
                        controller: 'RecipeCtrl',
                        controllerAs: 'Recipe'
                    })
                    .when('/ingredients', {
                        templateUrl: '/visit/ingredients',
                        controller: 'RecipeCtrl',
                        controllerAs: 'Recipe'
                    })
                    .when('/virtual-basket', {
                        templateUrl: '/visit/virtual-basket',
                        controller: 'RecipeCtrl',
                        controllerAs: 'Recipe'
                    })
                    .when('/settings', {
                        templateUrl: '/visit/settings',
                        controller: 'RecipeCtrl',
                        controllerAs: 'Recipe'
                    })
                    .otherwise({
                        redirectTo: '/recipes'
                    });
        }])
        .controller('AppCtrl', ['$http', '$scope', '$mdSidenav', '$location', function ($http, $scope, $mdSidenav, $location) {
            // Functions
            $scope.toggleSidenav = function (menuId) {
                $mdSidenav(menuId).toggle();
            };
            $scope.getActive = function(){
                return $scope.active_template;
            };
            $scope.base_url = function(string){
                if (string !== undefined){
                    return $location.protocol() + '://'+ $location.host()+":"+ $location.port() + '/'+ string;
                }else{
                    return $location.protocol() + '://'+ $location.host()+":"+ $location.port();
                }
                
            }
            $scope.menus = [
                {
                    icon: 'action:home',
                    title: 'recipes'
                },
                {
                    icon: 'action:home',
                    title: 'ingredients'
                },
                {
                    icon: 'action:shopping_basket',
                    title: 'virtual basket'
                },
                {
                    icon: 'action:settings',
                    title: 'settings'
                }
            ];
            $scope.active_template = $scope.menus[0];
        
        }])
        .controller('SideBarCtrl', ['$scope', '$location', function($scope, $location){
            $scope.toogleTemplate = function(index){
                $scope.$parent.active_template = $scope.$parent.menus[index];
                $location.path($scope.$parent.active_template.title.replace(" ", "-"));
            }
        }])
        .controller('RecipeCtrl', ['$http', '$scope', function($http, $scope){
            var config = {
                method: 'GET',
                withCredentials: true,
                url: $scope.$parent.base_url('api/recipe-types')
            };
            $http(config)
                .success(function(data, status, headers, config) {
                    console.log(data);
                })
                .error(function(data, status, headers, config) {
                    console.log('Testing console error');
                    console.log($scope.$parent.base_url('api/recipe-types'));
                });
        }]);
}());