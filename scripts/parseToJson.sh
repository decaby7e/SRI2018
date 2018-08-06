#!/bin/bash

SOURCEDEST="$1"
SAVEDEST="$2"
TITLE="$3"

/home/mininet/class-testing/joy/bin/joy entropy=1 bidir=1 retrans=1 classify=1 ppi=1 output=$SAVEDEST/$TITLE.gz $SOURCEDEST

/home/mininet/class-testing/joy/sleuth $SAVEDEST/$TITLE.gz > $SAVEDEST/$TITLE.json
