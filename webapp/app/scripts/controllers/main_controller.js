app.Controllers.Main = Marionette.Controller.extend({
  index: function() {
    'use strict';
    this.searchController = new app.Controllers.Search();
    this.listenTo(this.searchController, 'location:found', this.locationFound);
  },

  locationFound: function(data) {
    'use strict';

    var county = new app.Models.Entity(data.current.county),
        city = new app.Models.Entity(data.current.city),
        ids = new app.Models.Entity(data.current.ids);

    this.entities = new app.Collections.Entities();
    this.entities.push(county);
    this.entities.push(city);
    this.entities.push(ids);

    this.renderButtons();
    this.renderCounty(city);
    this.renderCity(city);
    this.renderIDS(ids);
  },

  renderCounty: function(county) {
    'use strict';
    this.countyLayout = new app.Layouts.EntityLayout();
    app.countyRegion.show(this.countyLayout);
    this.countyLayout.debtBox.show(new app.Views.Entity({
      model: county
    }));
  },

  renderCity: function(city) {
    'use strict';
    this.cityLayout = new app.Layouts.EntityLayout();
    app.cityRegion.show(this.cityLayout);
    this.cityLayout.debtBox.show(new app.Views.Entity({
      model: city
    }));
  },

  renderIDS: function(ids) {
    'use strict';
    this.isdRegion = new app.Layouts.EntityLayout();
    app.isdRegion.show(this.isdRegion);
    this.isdRegion.debtBox.show(new app.Views.Entity({
      model: ids
    }));
  },

  renderButtons: function() {
    'use strict';
    this.goToButtons = new app.Views.GoToButtons({
      collection: this.entities
    });

    app.goToRegion.show(this.goToButtons);
  }
});
