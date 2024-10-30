import pandas as pd
import matplotlib.pyplot as plt


class SupernovaeDataFrame:
    def __init__(self, file_path):
        """
        Initialize SupernovaeDataFrame with cosmic constants and load data from a file.
        
        Parameters:
            file_path (str): Path to the data file containing supernova records.
        """
        self.sn_data = []
        self.seconds_per_year = 52_600 * 60  # Seconds per year (approximate)
        self.universe_age_sec = 13_787_000_000 * self.seconds_per_year  # Cosmic time in seconds
        self.speed_of_light_kmps = 299_792.458  # Speed of light in km/s
        self.universe_radius_km = self.speed_of_light_kmps * self.universe_age_sec  # Radius in km
        self.universe_radius_ly = self.universe_radius_km / 9_460_730_472_580.8  # Radius in light-years

        # Load data from the file
        self._load_data(file_path)

        # Convert data to a DataFrame and plot results
        self._create_dataframe()

    def _load_data(self, file_path):
        """
        Load and parse data from the specified file, calculating properties for each supernova.
        
        Parameters:
            file_path (str): Path to the data file containing supernova records.
        """
        with open(file_path, "r") as file:
            first_record = True  # Skip header row
            
            for line in file:
                # Skip the header
                if first_record:
                    first_record = False
                    continue

                # Split the line and parse values
                columns = line.strip().split("\t")
                z = float(columns[0])  # Redshift
                d_proper_mpc = float(columns[1])  # Proper distance in Mpc
                d_err = float(columns[2])  # Distance error

                # Distance calculations
                d_proper_ly = d_proper_mpc * 3.26 * 1_000_000  # Convert to light-years
                d_comoving_mpc = d_proper_mpc / (z + 1)  # Comoving distance in Mpc
                d_comoving_ly = d_comoving_mpc * 3.26  # Convert comoving distance to million light-years

                # Velocity and universe age calculations
                velocity_fraction = (1 - 1 / (z + 1) ** 2) ** 0.5
                velocity_kmps = velocity_fraction * self.speed_of_light_kmps  # Velocity in km/s
                redshift_velocity = self.speed_of_light_kmps * z  # Redshift velocity
                age_of_universe_at_emission = self.universe_age_sec / (z + 1)  # Universe age at emission

                # Calculate R(z, t), representing distance based on cosmic age and redshift
                r_of_z_and_t = age_of_universe_at_emission * velocity_fraction

                # Append record
                record = [
                    z, d_proper_mpc, d_proper_ly, d_err, (z + 1),
                    velocity_fraction, velocity_kmps, d_comoving_mpc,
                    d_comoving_ly, r_of_z_and_t, age_of_universe_at_emission,
                    redshift_velocity
                ]
                self.sn_data.append(record)

    def _create_dataframe(self):
        """
        Create a pandas DataFrame from the parsed supernova data, display it,
        and plot the relationship between redshift and distance.
        """
        # Define column names and create DataFrame
        columns = [
            'z', 'd_proper_mpc', 'd_proper_ly', 'd_err', 'scale_factor',
            'velocity_fraction', 'velocity_kmps', 'd_comoving_mpc',
            'd_comoving_ly', 'r_of_z_and_t', 'age_of_universe', 'redshift_velocity'
        ]
        sn_df = pd.DataFrame(self.sn_data, columns=columns)
        print(sn_df)

        # Plot redshift vs. R(z, t)
        sn_df.plot(kind='scatter', x='z', y='r_of_z_and_t', color='purple')
        ax = plt.gca()
        ax.set_xlim([-0.05, 2])
        ax.set_xlabel('Redshift (z)')
        ax.set_ylabel('Distance R(z, t) (in cosmic units)')
        plt.title('Relationship between Redshift and Cosmic Distance R(z, t)')
        plt.show()


# Example usage
SupernovaeDataFrame("sn_data.txt")
