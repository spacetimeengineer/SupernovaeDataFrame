import pandas as pd
import matplotlib.pyplot as plt


class SupernovaeDataFrame:
    def __init__(self, file_path):
        """Initialize with cosmic constants, load data, and prepare DataFrame."""
        self.sn_data = []

        # Constants (short labels for equations)
        sec_per_yr = 52_600 * 60  # approx. seconds/year
        age_universe_sec = 13_787_000_000 * sec_per_yr  # cosmic time in seconds
        c_kmps = 299_792.458  # speed of light in km/s
        radius_universe_km = c_kmps * age_universe_sec  # radius in km
        radius_universe_ly = radius_universe_km / 9_460_730_472_580.8  # radius in ly

        # Store constants for use in methods
        self.sec_per_yr, self.age_universe_sec = sec_per_yr, age_universe_sec
        self.c_kmps, self.radius_universe_ly = c_kmps, radius_universe_ly

        self._load_data(file_path)  # Load data from file
        self._create_dataframe()  # Create DataFrame and plot results

    def _load_data(self, file_path):
        """Parse supernova data file, computing properties for each entry."""
        with open(file_path, "r") as file:
            first_record = True

            for line in file:
                if first_record:
                    first_record = False
                    continue

                # Parse line data
                columns = line.strip().split("\t")
                z, d_mpc, d_err = (
                    float(columns[0]),
                    float(columns[1]),
                    float(columns[2]),
                )

                # Distance calculations
                d_ly = d_mpc * 3.26e6  # Convert to ly
                d_com_mpc = d_mpc / (z + 1)
                d_com_ly = d_com_mpc * 3.26  # million ly

                # Velocity and cosmic age calculations
                v_frac = (1 - 1 / (z + 1) ** 2) ** 0.5
                v_kmps = v_frac * self.c_kmps
                rs_v = self.c_kmps * z  # Redshift velocity (short variable)
                ua_em = self.age_universe_sec / (
                    z + 1
                )  # Universe age at emission (short variable)

                # R(z, t) calculation
                r_zt = ua_em * v_frac

                # Record results
                record = [
                    z,
                    d_mpc,
                    d_ly,
                    d_err,
                    (z + 1),
                    v_frac,
                    v_kmps,
                    d_com_mpc,
                    d_com_ly,
                    r_zt,
                    ua_em,
                    rs_v,
                ]
                self.sn_data.append(record)

    def _create_dataframe(self):
        """Create DataFrame from parsed data, display and plot redshift vs. R(z, t)."""
        columns = [
            "z",
            "d_mpc",
            "d_ly",
            "d_err",
            "scale_factor",
            "v_frac",
            "v_kmps",
            "d_com_mpc",
            "d_com_ly",
            "r_zt",
            "universe_age",
            "redshift_v",
        ]
        sn_df = pd.DataFrame(self.sn_data, columns=columns)
        print(sn_df)

        # Plot redshift vs. R(z, t)
        sn_df.plot(kind="scatter", x="z", y="r_zt", color="purple")
        plt.gca().set(xlim=[-0.05, 2], xlabel="Redshift (z)", ylabel="Distance R(z, t)")
        plt.title("Redshift vs. Cosmic Distance R(z, t)")
        plt.show()


# Example usage
SupernovaeDataFrame("sn_data.txt")
