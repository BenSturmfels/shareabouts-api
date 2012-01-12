class ActivityController < ApplicationController

  def index
    respond_to do |format|
      format.json do
        since  = params[:utc] ? Time.at( params[:utc].to_i/1000 - Time.now.utc_offset ) : Date.today - 1000.years
        @activity_items = ActivityItem.where("created_at > '#{since.to_formatted_s(:psql)}'")
          .limit(params[:limit])
          .order('created_at desc')
        render "index.html"
      end
    end
  end
end