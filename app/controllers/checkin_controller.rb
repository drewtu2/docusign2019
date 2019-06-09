class CheckinController < ApplicationController
  def index
    @checkins = User.find(session[:user_id]).checkins.includes(:location).order('created_at DESC')
  end

  def new
    begin
    result = `python3 ./lib/scripts/checkin.py --lat 38.733082 --long -109.592514`
    location_name = result.split('\n').first
    rescue StandardError
      location_name = "Arches National Park"
    end
    location = Location.find_by_name(location_name)
    location = Location.create(name: location_name,lattitude: "38.733082", longitude: "-109.592514", state: "CA" ) unless location.present?
    name = "#{SecureRandom.urlsafe_base64}_#{location}.#{params['file'].path.split('.').last}"
    FileUtils.mv(params['file'].path,"#{Rails.root.to_s}/app/assets/images/#{name}")
    Checkin.create(user_id: session[:user_id],lattitude: "38.733082", longitude: "-109.592514", location: location, image: name )
    render json: {
      suceess: true
    }
  end
end
