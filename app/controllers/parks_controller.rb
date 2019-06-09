class ParksController < ApplicationController
  def index
    @parks = Location.all
  end
end
