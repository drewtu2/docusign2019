class CreateCheckins < ActiveRecord::Migration[5.2]
  def change
    create_table :checkins do |t|
      t.string :longitude
      t.string :lattitude
      t.string :image
      t.string :user_id
      t.integer :location_id
      t.timestamps
    end
  end
end
