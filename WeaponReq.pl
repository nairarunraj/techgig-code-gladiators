# Read input from STDIN. Print your output to STDOUT

sub get_cheapest_level {
	my $levelsView = shift;
	
	my $cheapestLevel;
	my $coinsReqdForCheapestLevel = 999999999;
	
	for my $currentLevel (keys(%{$levelsView})) {
		my $coinsReqdForThisLevel = (scalar(keys(%{$levelsView->{$currentLevel}}))) ** 2;
		if($coinsReqdForCheapestLevel > $coinsReqdForThisLevel) {
			$coinsReqdForCheapestLevel = $coinsReqdForThisLevel;
			$cheapestLevel = $currentLevel;
		}
	}
	
	return ($cheapestLevel, $coinsReqdForCheapestLevel);
}

sub remove_level {
	my $cheapestLevel = shift;
	my $levelsView = shift;
	
	my @weaponsInThisLevel = keys(%{$levelsView->{$cheapestLevel}});
	
	my @levelsToDelete;
	for my $currentLevel(keys(%{$levelsView})) {
		for my $acquiredWeapon(@weaponsInThisLevel) {
			delete $levelsView->{$currentLevel}->{$acquiredWeapon} if exists $levelsView->{$currentLevel}->{$acquiredWeapon};
		}
		push @levelsToDelete, $currentLevel if(scalar(keys(%{$levelsView->{$currentLevel}}))==0);
	}
	
	for my $accomplishedLevel (@levelsToDelete) {
		delete $levelsView->{$accomplishedLevel};
	}
	
	return;
}


sub main{

	chomp(my $mAndN = <STDIN>);
	my ($N, $M) = split / /, $mAndN;
	
	my @weaponsReq;
	for(0..$N) {
	    chomp(my $weaponsReqForThisLevel = <STDIN>);
	    push @weaponsReq, $weaponsReqForThisLevel;
	}
	
	my $levelsView;
	for(my $i=0; $i<=$#weaponsReq;$i++) {
	    my @currentLevelWeaponsReq = split //, $weaponsReq[$i];
	    for(my $j=0; $j<=$#currentLevelWeaponsReq;$j++) {
	        $levelsView->{$i}->{$j}=1 if($currentLevelWeaponsReq[$j]==1);
	    }
	}
	
	my $totalCoins;
	while(scalar(keys(%{$levelsView})) > 0) {
	    my ($cheapestLevel, $coinsReqdForCheapestLevel) = get_cheapest_level($levelsView);
	    
	    $totalCoins += $coinsReqdForCheapestLevel;
	    
	    remove_level($cheapestLevel, $levelsView);
	}

    print $totalCoins;
}
&main;