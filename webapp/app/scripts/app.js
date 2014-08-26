window.app = new Marionette.Application();

app.Collections = app.Collections || {};
app.Controllers = app.Controllers || {};
app.Layouts = app.Layouts || {};
app.Mixins = app.Mixins || {};
app.Models = app.Models || {};
app.Routers = app.Routers || {};
app.Views = app.Views || {};

app.Settings = {
  'baseURL': 'http://localhost:8000'
};

app.addRegions({
  'searchRegion': '#search',
  'searchStringRegion': '#search-string',
  'goToRegion' : '#go-to-buttons',
  'countyRegion': '#county-region',
  'cityRegion': '#city-region',
  'isdRegion': '#isd-region'
});

app.addInitializer(function() {
  'use strict';

  var mainController = new app.Controllers.Main();
  mainController.index();
});

$(document).ready(function(){
  'use strict';

  app.start();
});
