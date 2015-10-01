(function (){
    angular
        .module("infoApp", [
            'ui.bootstrap',
            'restangular'
        ])
        .config(config);

    config.$include = ['RestangularProvider'];
    function config(RestangularProvider) {
        RestangularProvider.setBaseUrl('/api');
        RestangularProvider.setResponseExtractor(function(response, operation) {
            return response.results;
        });
    }
})();