# Import the pandas library to handle tabular data structures (DataFrames).
import pandas as pd
# Import io to handle in-memory string data as file-like objects.
import io
# Import matplotlib to create data visualizations (e.g., redshift-distance plots).
import matplotlib.pyplot as plt




# Embedded astronomical data for universal expansion
# Columns: redshift (z), distance (d), and distance error (d_err)
raw_data = """
#z	d	d_err
0.01	51.5229	8.77905
0.01	43.6516	7.63887
0.01	55.4626	9.96117
0.013	63.6796	9.09091
0.013	55.7186	7.69781
0.014	66.9885	8.9463
0.014	66.6807	8.9052
0.014	76.913	10.2717
0.015	82.4138	10.6268
0.016	80.5378	10.014
0.016	66.9885	8.32932
0.016	76.2079	9.47566
0.016	79.4328	9.87665
0.017	68.5488	8.20765
0.017	78.343	9.38035
0.017	83.946	10.4378
0.017	87.4984	11.2825
0.017	87.0964	10.4284
0.018	98.1748	11.3028
0.018	72.1107	8.30206
0.019	82.7942	9.53204
0.021	102.329	10.8386
0.023	106.66	10.8061
0.023	117.49	11.9033
0.024	104.232	10.5601
0.025	120.226	12.1806
0.025	104.232	10.5601
0.026	130.017	12.5738
0.026	133.66	13.5415
0.026	117.49	12.4444
0.027	151.356	14.6374
0.028	127.644	12.9321
0.029	138.038	13.3495
0.029	168.267	16.2729
0.03	151.356	14.6374
0.031	147.231	14.2385
0.032	164.437	15.1452
0.033	127.644	12.3443
0.034	172.982	15.9322
0.036	159.221	15.398
0.036	171.396	15.7861
0.036	189.671	16.5958
0.038	215.774	18.8799
0.04	188.799	17.389
0.043	201.372	17.6197
0.045	250.035	20.7261
0.046	186.209	18.008
0.049	204.174	18.8051
0.05	233.346	23.6411
0.05	259.418	22.6986
0.052	270.396	22.4139
0.053	245.471	21.4783
0.056	289.734	25.3512
0.058	266.686	23.3345
0.061	289.734	29.3541
0.063	341.979	29.9226
0.071	359.749	31.4774
0.075	358.096	31.3328
0.079	387.258	32.101
0.088	411.15	53.0156
0.101	549.541	50.6146
0.124	688.652	69.7699
0.172	907.821	75.252
0.18	990.832	82.1331
0.249	1419.06	111.095
0.263	1492.79	116.868
0.278	1592.21	300.628
0.285	1527.57	119.59
0.3	1592.21	183.31
0.32	1949.84	161.629
0.331	1682.67	131.733
0.334	1527.57	211.041
0.337	1940.89	151.948
0.34	2004.47	156.926
0.357	2118.36	165.842
0.358	2147.83	168.149
0.369	2157.74	168.925
0.371	2157.74	168.925
0.38	2535.13	256.843
0.388	2594.18	226.986
0.4	2558.59	223.872
0.415	2466.04	193.061
0.416	2630.27	230.144
0.425	2177.71	401.149
0.43	2964.83	341.339
0.43	2924.15	457.851
0.43	2466.04	193.061
0.43	2500.35	207.261
0.44	2594.18	226.986
0.449	2570.4	201.231
0.45	2666.86	257.908
0.45	2630.27	278.595
0.455	2870.78	370.172
0.459	3419.79	346.472
0.46	2301.44	423.941
0.46	2792.54	411.524
0.461	2779.71	217.618
0.463	2844.46	222.687
0.47	3564.51	344.719
0.47	3515.6	372.369
0.47	3090.3	241.933
0.472	3104.56	271.643
0.474	3647.54	369.546
0.475	2805.43	258.39
0.477	2992.26	289.378
0.478	3133.29	331.874
0.48	2978.52	274.332
0.49	3019.95	347.685
0.495	2818.38	246.604
0.496	2964.83	232.11
0.5	3531.83	390.352
0.5	3515.6	323.799
0.504	3326.6	260.432
0.508	2741.57	441.89
0.511	3681.29	356.012
0.518	3681.29	525.542
0.526	3250.87	269.475
0.528	3564.51	410.38
0.532	3597.49	298.207
0.537	3715.35	701.503
0.538	3404.08	282.175
0.54	2466.04	465.618
0.543	3419.79	299.226
0.55	3419.79	267.729
0.552	3388.44	265.274
0.557	3467.37	271.453
0.57	3749.73	535.312
0.57	3630.78	418.009
0.571	3388.44	280.878
0.579	3732.5	326.587
0.58	4055.09	392.162
0.581	3357.38	293.764
0.582	4111.5	321.88
0.592	3548.13	310.455
0.604	3467.37	271.453
0.61	3944.57	308.812
0.613	4265.8	353.605
0.615	3715.35	393.526
0.62	4187.94	540.012
0.62	4385.31	363.512
0.627	3854.78	301.783
0.63	4487.45	764.623
0.633	4613.18	382.4
0.64	3999.45	460.453
0.643	4385.31	363.512
0.657	4508.17	415.218
0.67	4345.1	480.238
0.679	5199.96	454.987
0.688	4425.88	346.493
0.695	4385.31	383.707
0.707	4830.59	467.159
0.73	4943.11	409.749
0.735	4246.2	371.535
0.74	4742.42	480.472
0.74	4677.35	646.2
0.756	5345.64	418.499
0.771	4207.27	329.378
0.778	5780.96	931.781
0.791	5105.05	423.173
0.798	5970.35	852.329
0.8	5420.01	474.241
0.811	6698.85	956.329
0.811	6223	1003.03
0.815	5623.41	854.594
0.815	6576.58	848.015
0.822	5571.86	692.803
0.828	6194.41	1312.21
0.828	5223.96	1467.49
0.83	5888.44	515.228
0.832	5128.61	684.926
0.839	4897.79	451.103
0.84	5420.01	524.161
0.854	6194.41	827.263
0.86	6397.35	883.826
0.87	7177.94	1123.89
0.882	5997.91	828.642
0.884	6982.32	610.941
0.9	5345.64	615.44
0.905	5997.91	828.642
0.935	6223	831.082
0.949	5470.16	806.113
0.949	6309.57	697.36
0.95	6251.73	978.869
0.95	6729.77	960.743
0.954	5888.44	732.166
0.954	7244.36	900.761
0.961	6854.88	1041.74
0.97	8590.14	1424.13
0.975	6950.24	832.183
0.977	6053.41	724.801
1.01	8994.98	787.044
1.02	8016.78	701.454
1.02	6280.58	780.925
1.056	7413.1	785.188
1.12	8590.14	712.063
1.14	8749.84	1168.54
1.14	7726.81	1103.08
1.199	6886.52	1078.26
1.23	10814.3	1145.44
1.23	9862.79	908.397
1.3	10280.2	946.838
1.305	7979.95	1102.47
1.34	9638.29	1375.96
1.37	11117.3	1279.93
1.39	9549.93	835.602
1.755	11749	1893.71
""".strip()




class SupernovaExpansionAnalyzer:
    def __init__(self):
        """
        Initialize the analyzer with constants of cosmology and parse the supernova dataset.
        This constructor sets up:
        - Constants used for physical unit conversions.
        - The age of the universe (in seconds).
        - The maximum observable radius assuming constant speed of light.
        - The supernova dataset used to empirically explore cosmic expansion.
        """

        # Stores parsed data for each supernova as a list of numerical records.
        self.records = []

        # ---- CONSTANT DEFINITIONS (PHYSICAL AND COSMOLOGICAL) ----

        # Approximate number of seconds per year — 60 seconds * 60 minutes * 24 hours * ~365.25 days.
        # Here simplified as 52,600 minutes/year to speed up rough calculations.
        self.seconds_per_year = 52_600 * 60

        # Age of the universe in seconds.
        # 13.787 billion years (Planck 2018 value) multiplied by seconds per year.
        self.universe_age_seconds = 13_787_000_000 * self.seconds_per_year

        # Speed of light in kilometers per second — a fundamental limit in special relativity.
        self.speed_of_light_km_s = 299_792.458

        # Distance light has traveled since the Big Bang (in km), assuming flat space and constant c.
        radius_km = self.speed_of_light_km_s * self.universe_age_seconds

        # Convert radius from kilometers to light-years using the exact km-per-light-year conversion.
        self.universe_radius_ly = radius_km / 9_460_730_472_580.8

        # ---- PARSE THE DATA FILE ----
        # This function reads the tab-separated values file with columns:
        #   z (redshift), distance (in Mpc), and associated error.
        self._parse_supernova_data()

        # Create a structured DataFrame and generate plots from the parsed data.
        self._build_dataframe()

    def _parse_supernova_data(self):
        """
        Parses in-memory string data containing supernova measurements and performs
        cosmological calculations for each record.

        The raw_data string must have tab-separated values and can optionally begin
        with a header line starting with '#'.

        Each line must contain:
            - Redshift (z)
            - Distance (in Megaparsecs)
            - Distance error
        """
        # Treat the string as a file-like object
        file_like = io.StringIO(raw_data)

        for line in file_like:
            # Skip comments or headers
            if line.startswith("#"):
                continue

            # Parse the numerical values
            z, distance_mpc, distance_err = map(float, line.strip().split("\t"))

            # --- COSMOLOGICAL CONVERSIONS AND METRICS ---

            distance_ly = distance_mpc * 3.26e6
            comoving_distance_mpc = distance_mpc / (z + 1)
            comoving_distance_mly = comoving_distance_mpc * 3.26
            velocity_fraction = (1 - 1 / (z + 1) ** 2) ** 0.5
            velocity_km_s = velocity_fraction * self.speed_of_light_km_s
            redshift_velocity = self.speed_of_light_km_s * z
            universe_age_emission = self.universe_age_seconds / (z + 1)
            r_zt = universe_age_emission * velocity_fraction

            self.records.append([
                z,
                distance_mpc,
                distance_ly,
                distance_err,
                (z + 1),  # Scale factor
                velocity_fraction,
                velocity_km_s,
                comoving_distance_mpc,
                comoving_distance_mly,
                r_zt,
                universe_age_emission,
                redshift_velocity,
            ])

    def _build_dataframe(self):
        """
        Constructs a pandas DataFrame from the computed data.
        Also generates a scatter plot of redshift (z) vs. calculated R(z, t).
        """

        # Column names for the DataFrame.
        # These names reflect the physical or cosmological quantity calculated.
        columns = [
            "Redshift (z)",
            "Distance (Mpc)",
            "Distance (ly)",
            "Distance Error",
            "Scale Factor",
            "Velocity Fraction (v/c)",
            "Velocity (km/s)",
            "Comoving Distance (Mpc)",
            "Comoving Distance (MLy)",
            "R(z, t)",
            "Universe Age at Emission (s)",
            "Redshift Velocity (km/s)",
        ]

        # Construct a DataFrame using the records and labeled columns.
        self.dataframe = pd.DataFrame(self.records, columns=columns)

        # Print the full DataFrame to console for review or debugging.
        print(self.dataframe)

        # ---- DATA VISUALIZATION ----
        # Create a scatter plot showing the redshift (z) vs. computed distance R(z, t).
        # This helps visualize the universe’s expansion history.

        self.dataframe.plot(
            kind="scatter",
            x="Redshift (z)",      # Horizontal axis: how far back in time we're looking.
            y="R(z, t)",           # Vertical axis: inferred distance at emission using v*t.
            color="purple"
        )

        # Set axis limits and labels for clarity and scale appropriateness.
        plt.gca().set(
            xlim=[-0.05, 2],       # Redshift typically ranges from 0 to ~1.5 in supernova studies.
            xlabel="Redshift (z)",
            ylabel="Distance R(z, t)"
        )

        # Add plot title and grid to aid readability.
        plt.title("Redshift vs. Cosmic Distance R(z, t)")
        plt.grid(True)
        plt.tight_layout()

        # Display the plot window.
        plt.show()


# ----- SCRIPT ENTRY POINT -----
# If this script is run directly (not imported as a module), run the analysis.
if __name__ == "__main__":
    # Pass the path to your data file containing redshift + distance values.
    SupernovaExpansionAnalyzer()
