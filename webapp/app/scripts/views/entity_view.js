app.Views.Entity = Marionette.ItemView.extend({
  template: JST['app/scripts/templates/entity.html'],
  className: 'debt-entity',

  templateHelpers: function() {
    'use strict';

    var isACounty = this.model.get('issuerType') === 'county',
        isAIDS = this.model.get('issuerType') === 'isd',
        isACity = this.model.get('issuerType') === 'city';

    return {
      'isACounty': isACounty,
      'isAIDS': isAIDS,
      'isACity': isACity
    };
  },

  onRender: function() {
    'use strict';

    this.$el.addClass(this.model.get('issuerType'));
  }
});
