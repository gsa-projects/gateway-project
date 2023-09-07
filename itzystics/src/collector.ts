interface Platform {
    spotify?: string;
    apple_music?: string;
    youtube?: string;
    melon?: string;
    genie?: string;
    bugs?: string;
    flo?: string;
    vibe?: string;
}

class Music {
    name: string;
    isTitle: boolean;
    platform: Platform;
    mv?: string;

    constructor(name: string, platform: Platform, isTitle: boolean = false) {
        this.name = name;
        this.platform = platform;
        this.isTitle = isTitle;
    }

    setMv(mv: string) {
        this.mv = mv;
        return this;
    }
}

const enum AlbumType {
    SINGLE,
    DIGITAL_SINGLE,
    PRE_RELEASE,
    EP,
    ALBUM
}

const enum Country {
    KOR,
    JPN,
    USA
}

class Album {
    name: string;
    type: AlbumType;
    target: Country;
    musics: Music[] = [];

    constructor(name: string, cover: string, type: AlbumType = AlbumType.EP, target: Country = Country.KOR) {
        this.name = name;
        this.type = type;
        this.target = target;
    }

    addMusic(music: Music) {
        this.musics.push(music);
        return this;
    }
}

let a = new Music('wannabe', { spotify: 'spotify.com' });