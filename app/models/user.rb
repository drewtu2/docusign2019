class User < ApplicationRecord
  has_many :advocacies
  has_many :issues, through: :advocacies
  has_many :checkins
end
