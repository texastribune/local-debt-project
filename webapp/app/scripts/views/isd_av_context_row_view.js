app.Views.ISDAVContextRow = Marionette.ItemView.extend({
  template: JST['app/scripts/templates/isd_av_context_row.html'],
  tagName: 'tr'
});

_.extend(app.Views.ISDAVContextRow.prototype, app.Mixins.Helpers);
