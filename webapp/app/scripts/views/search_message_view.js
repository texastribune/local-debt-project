app.Views.SearchMessage = Marionette.ItemView.extend({
  template: JST['app/scripts/templates/search_message.html'],
  templateHelpers: function() {
    'use strict';
    return {
      'failed': this.model.get('status') === 'error'
    };
  }
});
