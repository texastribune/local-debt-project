window.app = new Marionette.Application();

app.Views = app.Views || {};
app.Models = app.Models || {};
app.Controllers = app.Controllers || {};
app.Routers = app.Routers || {};
app.Settings = {
  'baseURL': 'http://localhost:8000'
};

app.addRegions({
  'searchRegion': '#search',
  'cardsRegion': '#cards',
  'contextRegion': '#context'
});

app.Routers.Main = Backbone.Marionette.AppRouter.extend({
  appRoutes: {
    '': 'index'
  }
});

app.addInitializer(function() {
  'use strict';

  this.mainRouter = new app.Routers.Main( {
    controller: new app.Controllers.Main()
  });

  if ( Backbone.history ) {
    Backbone.history.start();
  }
});

$(document).ready(function(){
  'use strict';

  app.start();
});
