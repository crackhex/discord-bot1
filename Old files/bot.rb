require 'discordrb'

bot = Discordrb::Commands::CommandBot.new token: 'NDc4Mzg1NTkyNTQ0MDAyMDQ5.DlJ8sg.VkrWjFIQe9xzYwHj6ylZivnm5FY', client_id: 478385592544002049, prefix: '~'

bot.command(:cookie) do |event|
  event.respond ':cookie:'
end
bot.command(:oof) do |event|
  event.respond 'o0f'
end

bot.run

loop { sleep 10 }
