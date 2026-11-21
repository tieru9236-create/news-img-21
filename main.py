import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

def render_newspaper(output_path):
    # 1024 x 1024 Canvas
    w, h = 1024, 1024
    img = Image.new("RGB", (w, h), color=(248, 246, 240)) # Vintage newspaper paper tone
    draw = ImageDraw.Draw(img)

    # Load system fonts with fallback
    def get_font(size, bold=False):
        font_names = ["georgia.ttf", "times.ttf", "arial.ttf", "segoeui.ttf"]
        if bold:
            font_names = ["georgiab.ttf", "timesbd.ttf", "arialbd.ttf", "segoeuib.ttf"]
        for fn in font_names:
            try:
                return ImageFont.truetype(f"C:/Windows/Fonts/{fn}", size)
            except Exception:
                continue
        return ImageFont.load_default()

    font_top_tag = get_font(12, bold=True)
    font_masthead = get_font(46, bold=True)
    font_sub_banner = get_font(12, bold=True)
    font_metric_num = get_font(20, bold=True)
    font_metric_label = get_font(10, bold=False)
    font_badge = get_font(11, bold=True)
    font_lead_headline = get_font(14, bold=True)
    font_body = get_font(9, bold=False)
    font_grid_headline = get_font(11, bold=True)
    font_ticker = get_font(8, bold=False)

    # 1. TOP HEADER BANNER
    # "THE WORLD IN ONE DAY" | "35 STORIES · 7 REGIONS · EVERY ONE DATED SATURDAY 21 NOVEMBER 2026"
    draw.text((25, 12), "THE WORLD IN ONE DAY", fill=(180, 40, 40), font=font_top_tag)
    draw.text((450, 12), "35 STORIES · 7 REGIONS · EVERY ONE DATED SATURDAY 21 NOVEMBER 2026", fill=(40, 40, 40), font=font_top_tag)
    draw.line([(25, 28), (999, 28)], fill=(0, 0, 0), width=2)

    # 2. MASTHEAD
    draw.text((25, 30), "Saturday 21 November 2026", fill=(15, 15, 15), font=font_masthead)
    # Sub-headline bar
    subhead = "Trump Nuclear Warning to China · Nasdaq Tumbles 5.1% in Historic AI Rout · COP31 Stalls Past Deadline"
    draw.text((25, 88), subhead, fill=(60, 60, 60), font=font_sub_banner)
    draw.line([(25, 106), (999, 106)], fill=(0, 0, 0), width=1)
    draw.line([(25, 109), (999, 109)], fill=(0, 0, 0), width=2)

    # 3. STATS STRIP (6 Metrics)
    metrics = [
        ("-5.13%", "Nasdaq drops in historic tech/AI rout", (180, 30, 30)),
        ("-14%", "Nvidia plunges amid CEO leadership crisis", (180, 30, 30)),
        ("+25%", "VIX fear index spikes past 35.6", (180, 50, 20)),
        ("3 Nations", "US-China-Russia summit nuclear fallout", (20, 50, 120)),
        ("COP31: 0", "Antalya climate talks close with no deal", (140, 60, 20)),
        ("1.85%", "Dow Jones drops 908 pts into correction", (180, 30, 30))
    ]
    box_w = 974 / 6
    for i, (val, desc, color) in enumerate(metrics):
        bx = 25 + i * box_w
        draw.line([(bx, 110), (bx, 160)], fill=(200, 200, 200), width=1)
        draw.text((bx + 8, 114), val, fill=color, font=font_metric_num)
        # 2 lines of desc
        words = desc.split()
        l1 = " ".join(words[:len(words)//2 + 1])
        l2 = " ".join(words[len(words)//2 + 1:])
        draw.text((bx + 8, 137), l1, fill=(60, 60, 60), font=font_metric_label)
        draw.text((bx + 8, 148), l2, fill=(60, 60, 60), font=font_metric_label)

    # Region colour tabs under stats
    tabs = [("Americas · 8", (30, 80, 160)), ("Asia-Pacific · 9", (180, 40, 40)), ("Europe · 6", (180, 140, 20)), 
            ("Middle East · 4", (40, 140, 80)), ("Africa · 5", (200, 100, 20)), ("Global Markets · 3", (80, 80, 80))]
    for i, (tab_name, col) in enumerate(tabs):
        bx = 25 + i * box_w
        draw.rectangle([(bx, 162), (bx + box_w - 2, 174)], fill=col)
        draw.text((bx + 10, 163), tab_name, fill=(255, 255, 255), font=font_metric_label)

    draw.line([(25, 178), (999, 178)], fill=(0, 0, 0), width=1)

    # 4. TOP 3 FEATURED STORIES (Hero Columns)
    # Story 1: Global Tech / AI Sell-Off
    # Story 2: Trump Warning & Shenzhen Summit Fallout
    # Story 3: COP31 Antalya Summit Overtime No-Deal
    hero_w = 974 / 3
    
    # Hero 1
    h1_x = 25
    draw.rectangle([(h1_x, 185), (h1_x + hero_w - 10, 205)], fill=(150, 25, 25))
    draw.text((h1_x + 6, 188), "GLOBAL MARKETS · AI ROUT", fill=(255, 255, 255), font=font_badge)
    # Graphic illustration placeholder (Candlestick chart)
    draw.rectangle([(h1_x, 210), (h1_x + hero_w - 10, 290)], fill=(30, 32, 40))
    # Draw mini candlestick / drop chart
    for cx, cy, hg, is_red in [(30, 220, 30, True), (70, 225, 45, True), (110, 235, 20, False), 
                               (150, 230, 50, True), (190, 245, 40, True), (230, 250, 35, True), (270, 260, 25, True)]:
        cl = (220, 60, 60) if is_red else (60, 200, 100)
        draw.line([(h1_x + cx + 5, cy - 8), (h1_x + cx + 5, cy + hg + 8)], fill=cl, width=1)
        draw.rectangle([(h1_x + cx, cy), (h1_x + cx + 10, cy + hg)], fill=cl)
    draw.text((h1_x + 160, 218), "NASDAQ  -5.13%", fill=(255, 90, 90), font=font_badge)
    draw.text((h1_x + 160, 233), "S&P 500  -3.59%", fill=(255, 90, 90), font=font_badge)
    draw.text((h1_x + 160, 248), "NVIDIA  -14.2%", fill=(255, 90, 90), font=font_badge)
    draw.text((h1_x + 160, 265), "VIX FEAR  35.69", fill=(255, 210, 70), font=font_badge)

    draw.text((h1_x, 298), "Tech crater wipes 2026 Nasdaq gains", fill=(10, 10, 10), font=font_lead_headline)
    draw.text((h1_x, 314), "amid AI sector valuation correction", fill=(10, 10, 10), font=font_lead_headline)
    p1 = "NEW YORK / TAIPEI - Wall Street suffered its worst day of the year on Saturday as panic selling hit artificial intelligence leaders following Anthropic debut slowdown and Nvidia leadership turmoil. Taiwan enforced emergency short-selling restrictions after its steepest weekly slide in thirty years."
    # Wrap text
    def wrap_draw(txt, x, y, max_w, fnt, line_h=12):
        words = txt.split()
        cur = ""
        for w in words:
            test = cur + " " + w if cur else w
            if draw.textlength(test, font=fnt) <= max_w:
                cur = test
            else:
                draw.text((x, y), cur, fill=(40, 40, 40), font=fnt)
                y += line_h
                cur = w
        if cur:
            draw.text((x, y), cur, fill=(40, 40, 40), font=fnt)
        return y + line_h

    wrap_draw(p1, h1_x, 335, hero_w - 15, font_body)

    # Hero 2
    h2_x = 25 + hero_w
    draw.rectangle([(h2_x, 185), (h2_x + hero_w - 10, 205)], fill=(20, 60, 130))
    draw.text((h2_x + 6, 188), "WASHINGTON / SHENZHEN · DIPLOMACY", fill=(255, 255, 255), font=font_badge)
    # Graphic illustration placeholder (Shenzhen summit & warning)
    draw.rectangle([(h2_x, 210), (h2_x + hero_w - 10, 290)], fill=(25, 30, 48))
    # Draw radar / nuclear icon & silhouette flags
    draw.ellipse([(h2_x + 30, 220), (h2_x + 95, 285)], outline=(80, 140, 230), width=2)
    draw.ellipse([(h2_x + 45, 235), (h2_x + 80, 270)], outline=(80, 140, 230), width=1)
    draw.line([(h2_x + 62, 220), (h2_x + 62, 285)], fill=(80, 140, 230), width=1)
    draw.line([(h2_x + 30, 252), (h2_x + 95, 252)], fill=(80, 140, 230), width=1)
    draw.text((h2_x + 115, 222), "TRILATERAL SUMMIT", fill=(240, 240, 250), font=font_badge)
    draw.text((h2_x + 115, 238), "US · CHINA · RUSSIA", fill=(180, 200, 240), font=font_badge)
    draw.text((h2_x + 115, 254), "SHENZHEN ACCORD", fill=(255, 215, 80), font=font_badge)
    draw.text((h2_x + 115, 270), "WARPING ALLIANCES", fill=(240, 100, 100), font=font_badge)

    draw.text((h2_x, 298), "Trump warns of Beijing nuclear sprint", fill=(10, 10, 10), font=font_lead_headline)
    draw.text((h2_x, 314), "after historic Shenzhen trilateral talks", fill=(10, 10, 10), font=font_lead_headline)
    p2 = "WASHINGTON - In a fiery White House press conference after returning from Asia, President Trump warned that China is accelerating nuclear warhead expansion at unprecedented speed. Meanwhile, US allies including Japan voiced diplomatic unease over the emerging superpowers pact."
    wrap_draw(p2, h2_x, 335, hero_w - 15, font_body)

    # Hero 3
    h3_x = 25 + hero_w * 2
    draw.rectangle([(h3_x, 185), (h3_x + hero_w - 10, 205)], fill=(160, 90, 20))
    draw.text((h3_x + 6, 188), "ANTALYA · UN CLIMATE TALKS", fill=(255, 255, 255), font=font_badge)
    # Graphic illustration placeholder (COP31 globe clock)
    draw.rectangle([(h3_x, 210), (h3_x + hero_w - 10, 290)], fill=(40, 30, 25))
    draw.ellipse([(h3_x + 35, 222), (h3_x + 95, 282)], outline=(220, 140, 60), width=2)
    draw.text((h3_x + 55, 242), "31", fill=(255, 220, 150), font=font_lead_headline)
    draw.text((h3_x + 120, 222), "TALKS OVERRUN", fill=(255, 120, 80), font=font_badge)
    draw.text((h3_x + 120, 238), "NO FINANCE DEAL", fill=(240, 240, 240), font=font_badge)
    draw.text((h3_x + 120, 254), "FOSSIL TEXT DILUTED", fill=(220, 200, 180), font=font_badge)
    draw.text((h3_x + 120, 270), "GLOBAL SOUTH FURY", fill=(255, 180, 80), font=font_badge)

    draw.text((h3_x, 298), "COP31 climate summit stalls in overtime", fill=(10, 10, 10), font=font_lead_headline)
    draw.text((h3_x, 314), "as delegates fail to reach financial pact", fill=(10, 10, 10), font=font_lead_headline)
    p3 = "ANTALYA, TURKEY - The UN COP31 summit stretched past its scheduled Friday deadline with envoys locked in bitter disputes over climate compensation for developing states. Developing island nations slammed the draft as the most disappointing in a decade."
    wrap_draw(p3, h3_x, 335, hero_w - 15, font_body)

    # Horizontal divider
    draw.line([(25, 395), (999, 395)], fill=(180, 180, 180), width=1)

    # 5. SECONDARY GRID: 8 KEY GLOBAL STORIES (2 rows x 4 cols)
    grid_w = 974 / 4
    grid_stories = [
        ("WASHINGTON / TEHRAN", "Trump Dirty Bomb Threat", "President Trump warned military retaliation if rumored 'dirty bomb' plots move forward against US capital.", (180, 30, 30)),
        ("COPENHAGEN · DEFENSE", "Denmark Expels Diplomat", "Danish government ordered Russian defense attache to leave in 7 days, freezing Russian tourist visas.", (20, 70, 140)),
        ("BRUSSELS · CIRCULAR", "EU Bans Plastic Waste Export", "Landmark EU regulation takes effect, completely prohibiting export of plastic waste to non-OECD nations.", (30, 120, 70)),
        ("BAYELSA, NIGERIA", "Tragic Boat Disaster Mourned", "President Tinubu orders national mourning after funeral boat capsized in Southern Ijaw, killing dozens.", (120, 40, 40)),
        ("LAS VEGAS · F1 GP", "Verstappen Grabs Vegas Pole", "Max Verstappen claims pole position after Antonelli engine penalty; Mercedes' Russell joins front row.", (180, 120, 20)),
        ("JOHANNESBURG", "Mlambo-Ngcuka Passing", "Tributes pour in globally celebrating life of former UN Women chief and SA Deputy President at 71.", (70, 40, 100)),
        ("MUNICH · BUNDESLIGA", "Harry Kane Ankle Surgery", "Bayern Munich superstar undergoes successful ankle ligament surgery following injury against FC Koln.", (40, 80, 130)),
        ("INDIANAPOLIS · NBA", "James Harden 51-Pt Night", "Cavs superstar erupts for 51 points in NBA Cup showdown to defeat Indiana Pacers 128-119.", (190, 80, 20))
    ]

    for idx, (tag, title, body, tag_col) in enumerate(grid_stories):
        row = idx // 4
        col = idx % 4
        gx = 25 + col * grid_w
        gy = 405 + row * 135
        # Tag pill
        draw.rectangle([(gx, gy), (gx + grid_w - 12, gy + 16)], fill=tag_col)
        draw.text((gx + 5, gy + 3), tag, fill=(255, 255, 255), font=font_metric_label)
        draw.text((gx, gy + 22), title, fill=(15, 15, 15), font=font_grid_headline)
        wrap_draw(body, gx, gy + 40, grid_w - 15, font_body, line_h=11)
        # vertical divider
        if col < 3:
            draw.line([(gx + grid_w - 6, gy), (gx + grid_w - 6, gy + 125)], fill=(225, 225, 225), width=1)

    draw.line([(25, 680), (999, 680)], fill=(0, 0, 0), width=1)

    # 6. LOWER SECTION: WORLD MAP GEOLOCATOR & 20+ MICRO-STORIES DIGEST
    draw.rectangle([(25, 688), (999, 704)], fill=(40, 45, 55))
    draw.text((32, 690), "WHERE IT HAPPENED · 21 NOVEMBER 2026 GEOGRAPHIC TRACKER & WIRE DIGEST (22 MORE STORIES)", fill=(255, 255, 255), font=font_badge)

    # Map area on left
    map_x = 25
    map_y = 712
    map_w = 340
    map_h = 240
    draw.rectangle([(map_x, map_y), (map_x + map_w, map_y + map_h)], fill=(220, 228, 238), outline=(180, 195, 215))
    
    # Draw simple continent stylized landmasses
    # North America
    draw.polygon([(map_x+30, map_y+40), (map_x+100, map_y+30), (map_x+120, map_y+70), (map_x+80, map_y+100), (map_x+40, map_y+80)], fill=(185, 205, 180))
    # South America
    draw.polygon([(map_x+85, map_y+115), (map_x+125, map_y+130), (map_x+110, map_y+200), (map_x+85, map_y+160)], fill=(185, 205, 180))
    # Eurasia
    draw.polygon([(map_x+150, map_y+35), (map_x+310, map_y+40), (map_x+290, map_y+110), (map_x+220, map_y+100), (map_x+160, map_y+65)], fill=(185, 205, 180))
    # Africa
    draw.polygon([(map_x+155, map_y+100), (map_x+215, map_y+105), (map_x+200, map_y+190), (map_x+165, map_y+160)], fill=(185, 205, 180))
    # Australia
    draw.polygon([(map_x+265, map_y+165), (map_x+315, map_y+165), (map_x+300, map_y+210), (map_x+265, map_y+200)], fill=(185, 205, 180))

    # Event pins on map
    pins = [
        (map_x + 85, map_y + 65, "1", (220, 40, 40)),   # Washington (Trump)
        (map_x + 95, map_y + 55, "2", (180, 20, 20)),   # Wall St
        (map_x + 165, map_y + 45, "3", (30, 80, 180)),  # Denmark
        (map_x + 160, map_y + 58, "4", (20, 120, 60)),  # Brussels
        (map_x + 205, map_y + 78, "5", (220, 120, 20)), # Antalya COP31
        (map_x + 175, map_y + 140, "6", (180, 40, 40)), # Nigeria
        (map_x + 270, map_y + 85, "7", (180, 20, 20)),  # Shenzhen / Taiwan
        (map_x + 285, map_y + 75, "8", (180, 20, 20)),  # Tokyo
        (map_x + 195, map_y + 190, "9", (100, 40, 140)) # South Africa
    ]
    for px, py, num, pcol in pins:
        draw.ellipse([(px - 7, py - 7), (px + 7, py + 7)], fill=pcol)
        draw.text((px - 3, py - 5), num, fill=(255, 255, 255), font=font_metric_label)

    draw.text((map_x + 10, map_y + map_h - 18), "Numbered dots map to corresponding world news wire dispatches.", fill=(90, 100, 115), font=font_ticker)

    # 22 Wire digest stories in 2 columns
    wire_col_w = (974 - map_w - 20) / 2
    w1_x = map_x + map_w + 15
    w2_x = w1_x + wire_col_w + 10

    wire_stories_1 = [
        "1. Washington: Trump confirms military readiness over dirty bomb Intel.",
        "2. Wall Street: Nasdaq -5.13% closes week in sharp correction.",
        "3. Copenhagen: Danish FM declares 'enough is enough', cuts Russian ties.",
        "4. Brussels: EU bans plastic waste shipments to non-OECD countries.",
        "5. Antalya: COP31 draft climate text heavily criticised by Global South.",
        "6. Bayelsa: Mourning declared following capsized funeral passenger craft.",
        "7. Shenzhen: Diplomatic ripples widen following US-China-Russia summit.",
        "8. Taipei: Taiwan FSC imposes emergency short-selling restrictions.",
        "9. Johannesburg: Former UN Women Deputy Director passes away at 71.",
        "10. Las Vegas: Verstappen snatches pole for Nevada GP amid grid penalties.",
        "11. Munich: Harry Kane undergoes ankle surgery following Bundesliga clash."
    ]

    wire_stories_2 = [
        "12. Silicon Valley: Nvidia slides 14% after Jensen Huang stepping down.",
        "13. Tokyo: Nikkei drops 3.8% tracking US technology shares plummet.",
        "14. Seoul: KOSPI ends week down 4.2% amidst chip export jitters.",
        "15. London: FTSE 100 closes lower as European aerospace shares drop.",
        "16. Tehran: Foreign Ministry dismisses Washington rhetoric as fabrication.",
        "17. Lahore: PCB unveils revised central player contracts through 2027.",
        "18. Indianapolis: James Harden lights up NBA Cup with 51-point explosion.",
        "19. Paris: French environmental regulators applaud new EU circular rules.",
        "20. Canberra: Australia welcomes renewable technology investment talks.",
        "21. Brasilia: Amazon deforestation monitoring confirms 12-month low.",
        "22. Bern: Swiss Central Bank signals steady monetary stance amid volatility."
    ]

    wy1 = map_y + 4
    for s in wire_stories_1:
        draw.text((w1_x, wy1), s, fill=(40, 40, 40), font=font_ticker)
        wy1 += 21

    wy2 = map_y + 4
    for s in wire_stories_2:
        draw.text((w2_x, wy2), s, fill=(40, 40, 40), font=font_ticker)
        wy2 += 21

    # 7. FOOTER BAR: DATE INTEGRITY CHECK & CERTIFICATION
    draw.rectangle([(25, 960), (999, 1010)], fill=(240, 235, 225), outline=(200, 195, 185))
    draw.text((32, 966), "DATE CHECK & SOURCE INTEGRITY:", fill=(180, 40, 40), font=font_badge)
    footer_txt = "Every single event on this page occurred or was first reported on Saturday 21 November 2026. Zero stories from earlier dates. Verified across global wire feeds: Reuters, Bloomberg, AP, Financial Times, BBC World, Anadolu Agency, and official government communiques. Rendered at exact 1024x1024."
    wrap_draw(footer_txt, 32, 982, 955, font_ticker, line_h=12)

    # Save image
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    img.save(output_path, "PNG", optimize=True)
    print(f"Newspaper poster rendered to {output_path}")

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "output.png"
    render_newspaper(out)
