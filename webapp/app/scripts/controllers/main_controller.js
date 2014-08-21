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
        isd = new app.Models.Entity(data.current.isd);

    this.entities = new app.Collections.Entities();
    this.entities.push(county);
    this.entities.push(city);
    this.entities.push(isd);

    this.renderButtons();
    this.renderCounty(county);
    this.renderCity(city);
    this.renderISD(isd);
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

  renderISD: function(isd) {
    'use strict';
    this.isdRegion = new app.Layouts.EntityLayout();
    app.isdRegion.show(this.isdRegion);
    this.isdRegion.debtBox.show(new app.Views.Entity({
      model: isd
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
