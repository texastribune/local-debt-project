app.Views.Entity = Marionette.ItemView.extend({
  template: JST['app/scripts/templates/entity.html'],
  className: 'debt-entity',

  onRender: function() {
    'use strict';

    this.$el.addClass(this.model.get('issuerType'));
  }
});

_.extend(app.Views.Entity.prototype, app.Mixins.Helpers);
