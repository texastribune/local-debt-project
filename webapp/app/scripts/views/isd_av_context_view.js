app.Views.ISDAVContext = Marionette.CompositeView.extend({
  template: JST['app/scripts/templates/isd_av_context.html'],
  childView: app.Views.ISDAVContextRow,
  childViewContainer: 'tbody',
});
