module ParksHelper
  IMAGES = %w(artic_refuge.gif background.jpg central_cali.jpg chaco_canyon.jpeg channel.jpg
      joshua.jpg malibu.jpg mojave.jpg topanga.jpg whiskeytown.jpg yosemite.jpg)
  def get_random_image
    IMAGES[Random.new.rand(0..10)]
  end
end
