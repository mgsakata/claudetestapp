# Dog slideshow — image vetting

The slideshow draws **only** from `vetted_dogs.json`, a pinned list of Wikimedia
Commons file titles that were reviewed by hand.

## Why the list is pinned

The page originally queried `Category:Quality images of dogs` live. On Commons,
*Quality image* is a **technical** rating — sharpness, exposure, composition. It
says nothing about subject matter, and the category is open for anyone to add to.
It contained, among other things, a photograph of a dog that had just been shot.

Filtering titles and descriptions by keyword is **not** sufficient on its own: in
the audit below, keyword matching produced 3 false positives for every true one,
and it only caught the dead-dog photo because the uploader happened to name the
file "Recently shot Greenland dog". A neutral filename would have passed.

## What was done

- Pool: deep search of `Quality images` intersected with all dog categories → 386 files.
- Every one of the 386 was reviewed visually, not just by metadata.
- 144 rejected, **242 kept**.

## Rejected for content

**Dead, injured or unwell animals**

- `Recently shot Greenland dog upernavik 2007-07-02 edited.jpg`
- `Dog hybrid from Venezuela.jpg`
- `Литохоро, собака на Святого Николая (3).jpg`
- `Космодром Байконур, собака на Гагаринском старте (3).jpg`
- `Байконур, собака на Королёва (1).jpg`
- `Four puppies drinking their mother's milk, standing on a dirt road in Don Khon Laos.jpg`

**Sexually explicit artwork (Roman frescoes, Naples museum)**

- `Napoli - Museo archeologico nazionale 4104.jpg`
- `Napoli - Museo archeologico nazionale 4105.jpg`
- `Napoli - Museo archeologico nazionale 4110.jpg`

**Confinement, restraint or poor conditions**

- `Пёс цепной и будка.jpg`
- `Caminata por los perros y animales Maracaibo 2012 (23).jpg`
- `Rottweiler in Sylhet 01.jpg`
- `Greyhound Racing 2 amk.jpg`
- `Greyhound Racing amk.jpg`
- `Świerklaniec wyścigi chartów 12.06.2010 ch. afgański 2p.jpg`
- `Торетам, щенок на платформе Пригородная.jpg`
- `Балхаш, собака в микрорайоне Мухаммеджанова (1).jpg`
- `Гелати, собака у монастыря (1).jpg`
- `Гелати, собака у монастыря (2).jpg`

**Medical / anatomical**

- `Exhibits of the Nienburg Museum 15.jpg`
- `Puppy with a blow-up collar (53254).jpg`

**Death-adjacent subjects (memorials, graves, dead game in paintings)**

- `At Victoria and Albert Museum 2024 016.jpg`
- `Gipsy (53560).jpg`
- `Dog in GWC (42535).jpg`
- `15-07-05-Schloß-Caputh-RalfR-N3S 1492.jpg`
- `Le Christ chez Marthe et Marie - Joos Goemaere.jpg`
- `Kiwi zone board in Okarito.jpg`

**Firearms present**

- `Kazakh shepard with dogs and horse.jpg`

## Rejected as off-topic

The remaining rejections contain no live dog as the subject — statues, museum
pieces, paintings, warning signs, dog-shaped balloons, corn dogs and hot-dog
stands, landscapes where a dog is a speck, and buildings that merely sit in a
dog-related category.

## Refreshing the list

Commons keeps growing, so this snapshot goes stale rather than wrong — new photos
simply never appear. To add more, repeat the audit: pull the current pool, diff it
against `vetted_dogs.json`, and review only the new titles **visually** before
appending them. Do not re-point the template at a live category query.
