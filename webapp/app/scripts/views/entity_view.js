app.Views.Entity = Marionette.ItemView.extend({
  template: JST['app/scripts/templates/entity.html'],
  className: 'debt-entity',

  templateHelpers: function() {
    'use strict';

    var isACounty = this.model.get('issuerType') === 'county',
        isISD = this.model.get('issuerType') === 'isd',
        isACity = this.model.get('issuerType') === 'city';

    return {
      'isACounty': isACounty,
      'isISD': isISD,
      'isACity': isACity
    };
  },

  onRender: function() {
    'use strict';

    this.$el.addClass(this.model.get('issuerType'));
  }
});
