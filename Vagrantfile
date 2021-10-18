Vagrant.configure(2) do |config|

  # Starts Juniper router
  (1..1).each do |i|
    config.vm.define "r#{i}" do |r|
      r.vm.box = "juniper/ffp-12.1X47-D15.4-packetmode"
      r.vm.provider "virtualbox" do |vb|
        vb.memory = 1024
        vb.cpus = 4
        vb.gui = false
      end
      r.vm.host_name = "r#{i}"
      r.vm.network :forwarded_port, guest: 22, host: "221#{i}", id: 'ssh'
      (1..7).each do |j|
        r.vm.network "private_network",
                        ip: "192.168.#{i}#{j}.1",
                        virtualbox__intnet: "r#{i}-tobj#{j}"
      end

    end
  end

  # Starts devices
  (1..1).each do |i|
    (1..6).each do |j|
      config.vm.define "to#{i}#{j}" do |tobj|
        tobj.vm.box = "ubuntu/focal64"
        tobj.vm.synced_folder ".", "/home/vagrant/botenv"
        tobj.vm.provider "virtualbox" do |vb|
          vb.memory = 512
          vb.cpus = 2
          vb.gui = false
        end
        tobj.vm.host_name = "to#{i}#{j}"
        tobj.vm.network :forwarded_port, guest: 22, host: "22#{i+2}#{j}", id: 'ssh'
        tobj.vm.network "private_network",
                        ip: "192.168.#{i}#{j}.2",
                        #ip: "192.168.22.#{i}#{j}",
                        virtualbox__intnet: "r#{i}-tobj#{j}"
                        #virtualbox__intnet: "r-tobj"
        tobj.vm.provision "shell", 
                        run: "always",
                        inline: "sudo apt-get update ;
                        sudo apt-get install -f supervisor ; 
                        sudo adduser admin1 ; 
                        sudo usermod -aG sudo admin1 ; 
                        cp /home/vagrant/.bash_aliases /home/admin1/.bash_aliases ; 
                        sudo apt-get install -f telnetd ; 
                        sudo apt-get -y install -f python3-pip ; 
                        sudo pip3 install pyinotify scapy numpy ; 
                        apt-get install net-tools ; echo 'alias gwon=\"sudo route add default gw 192.168.#{i}#{j}.1\"\nalias gwoff=\"sudo route del default gw 192.168.#{i}#{j}.1\"' > .bash_aliases ;
                        source ~/.bashrc ; 
                        route add default gw 192.168.#{i}#{j}.1"
      end
    end
  end

   # Starts vulnerable devices
   (1..1).each do |i|
     (7..7).each do |j|
       config.vm.define "to#{i}#{j}" do |tobj|
         tobj.vm.box = "elkinaguas/tiny-object-20"
         tobj.vm.synced_folder ".", "/home/vagrant/botenv"
         tobj.vm.provider "virtualbox" do |vb|
           vb.memory = 512
           vb.cpus = 2
           vb.gui = false
         end
         tobj.vm.host_name = "to#{i}#{j}"
         tobj.vm.network :forwarded_port, guest: 22, host: "22#{i+2}#{j}", id: 'ssh'
         tobj.vm.network "private_network",
                         ip: "192.168.#{i}#{j}.2",
                         virtualbox__intnet: "r#{i}-tobj#{j}"
         tobj.vm.provision "shell", 
                         run: "always",
                         inline: "sudo apt-get update ;
                         sudo apt-get install -f supervisor ; 
                         sudo adduser admin1 ; 
                         sudo usermod -aG sudo admin1 ; 
                         cp /home/vagrant/.bash_aliases /home/admin1/.bash_aliases ; 
                         sudo apt-get install -f telnetd ; 
                         sudo apt-get -y install -f python3-pip ; 
                         sudo pip3 install pyinotify scapy numpy ; 
                         apt-get install net-tools ; echo 'alias gwon=\"sudo route add default gw 192.168.#{i}#{j}.1\"\nalias gwoff=\"sudo route del default gw 192.168.#{i}#{j}.1\"' > .bash_aliases ;
                         source ~/.bashrc ; 
                         mkdir 192.168.11.5 ;
                         route add default gw 192.168.#{i}#{j}.1"
       end
     end
   end


  # Starts command & control server
  (1..1).each do |i|
    config.vm.define "cc" do |cc|
      cc.vm.box = "elkinaguas/tiny-object-20"
      cc.vm.synced_folder ".", "/home/vagrant/botenv"
      cc.vm.provider "virtualbox" do |vb|
        vb.memory = 512
        vb.cpus = 2
        vb.gui = false
      end
      cc.vm.host_name = "cc"
      cc.vm.network :forwarded_port, guest: 22, host: "2314", id: 'ssh'
      cc.vm.network "private_network",
                      ip: "192.168.11.4",
                      virtualbox__intnet: "r1-tobj1"
      cc.vm.provision "shell", 
                      run: "always",
                      inline: "apt-get install net-tools ; echo 'alias gwon=\"sudo route add default gw 192.168.1#{i}#{j}.1\"\nalias gwoff=\"sudo route del default gw 192.168.1#{i}#{j}.1\"' > .bash_aliases ;
                      source ~/.bashrc ; route add default gw 192.168.1#{i}#{j}.1"
    end
  end

  # Starts loader server
  (1..1).each do |i|
    config.vm.define "loader" do |loader|
      loader.vm.box = "elkinaguas/tiny-object-20"
      loader.vm.synced_folder ".", "/home/vagrant/botenv"
      loader.vm.provider "virtualbox" do |vb|
        vb.memory = 512
        vb.cpus = 2
        vb.gui = false
      end
      loader.vm.host_name = "loader"
      loader.vm.network :forwarded_port, guest: 22, host: "2315", id: 'ssh'
      loader.vm.network "private_network",
                      ip: "192.168.11.5",
                      virtualbox__intnet: "r1-tobj1"
      loader.vm.provision "shell", 
                      run: "always",
                      inline: " ls ;
                      cp ./botenv/bot_files/bot_files.tar.gz /home/admin1/ ;
                      sudo apt-get update ; sudo apt-get -y install vsftpd ;
                      apt-get install net-tools ; echo 'alias gwon=\"sudo route add default gw 192.168.1#{i}#{j}.1\"\nalias gwoff=\"sudo route del default gw 192.168.1#{i}#{j}.1\"' > .bash_aliases ;
                      source ~/.bashrc ; route add default gw 192.168.1#{i}#{j}.1"
    end
  end

end
